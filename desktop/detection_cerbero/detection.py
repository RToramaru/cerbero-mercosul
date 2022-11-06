import cv2
import numpy as np
import onnxruntime as ort
import easyocr
import psycopg2
import datetime
import base64

class Detection(str):
    def __init__(self, video):
        super().__init__()
        # funcao para obter a placa na proporcao 640x640 
        def box_bounding(im, color=(114, 114, 114)):
            # obtem a largura e altura da imagem
            shape = im.shape[:2]
            ratio = min(640 / shape[0], 640 / shape[1])
            # obtem a nova largura e altura da imagem
            new_padding = int(round(shape[1] * ratio)), int(round(shape[0] * ratio))
            width, height = 640 - new_padding[0], 640 - new_padding[1]
            width /= 2 
            height /= 2
            # cria uma nova imagem com a proporcao 640x640
            if shape[::-1] != new_padding:
                im = cv2.resize(im, new_padding, interpolation=cv2.INTER_LINEAR)
            top, bottom = int(round(height - 0.1)), int(round(height + 0.1))
            left, right = int(round(width - 0.1)), int(round(width + 0.1))
            # cria uma borda na imagem
            im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
            return im, ratio, (width, height)

        # obter o video da camera
        self.cap = cv2.VideoCapture(video)
        # carregar o modelo de deteccao de placa
        self.session = ort.InferenceSession("model_onnx/plate.onnx", providers=['CPUExecutionProvider'])
        # carregar o modelo de reconhecimento de caracteres
        self.reader = easyocr.Reader(['en'], gpu=False)
        # configurar o banco de dados
        self.con = psycopg2.connect(host='localhost', database='cerbero', user='postgres', password='1234')
        self.cur = self.con.cursor()

        # pecorre o video obtendo cada frame
        while self.cap.isOpened():
            _, self.img = self.cap.read()
            # obtem a imagem, passa para a funcao e obtem a nova imagem com a borda
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.image = self.img.copy()
            self.image, self.ratio, width_height = box_bounding(self.image)
            # transforma a imagem nas caracteristicas da rede
            self.image = self.image.transpose((2, 0, 1))
            self.image = np.expand_dims(self.image, 0)
            self.image = np.ascontiguousarray(self.image)
            self.im = self.image.astype(np.float32)
            self.im /= 255
            # obtem as entradas e saidas da rede
            self.outname = [i.name for i in self.session.get_outputs()]
            self.inname = [i.name for i in self.session.get_inputs()]
            self.inp = {self.inname[0]:self.im}
            # faz a inferencia da rede
            self.outputs = self.session.run(self.outname, self.inp)[0]
            self.ori_images = [self.img.copy()]

            # obtem as coordenadas da placa
            for i,(batch_id, x0, y0, x1, y1, cls_id, score) in enumerate(self.outputs):
                # verifica se o score da placa e maior que 0.9
                if(score > 0.9):
                    # obtem as coordenadas da placa e corta a imagem nas coordenadas
                    image = self.ori_images[int(batch_id)]
                    self.box = np.array([x0,y0,x1,y1])
                    self.box -= np.array(width_height*2)
                    self.box /= self.ratio
                    self.box = self.box.round().astype(np.int32).tolist()
                    self.plate = image[self.box[1]:self.box[3],self.box[0]:self.box[2]]
                    # converte a imagem para tons de cinza
                    self.grayPlate = cv2.cvtColor(self.plate, cv2.COLOR_BGR2GRAY)
                    # aplica o threshold na imagem
                    self.th2 = cv2.adaptiveThreshold(self.grayPlate,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,4)
                    self.height, _ = self.th2.shape[:2]
                    self.x = 318 / self.height
                    # redimensiona a imagem para 318x318
                    self.th2 = cv2.resize(self.th2, (0, 0), fx=self.x, fy=self.x, interpolation=cv2.INTER_AREA)
                    self.height, self.width = self.th2.shape[:2]
                    # obtem os contornos da imagem
                    self.contours, _ = cv2.findContours(self.th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    self.contours_list = []
                    # cria uma lista com os contornos mais proximos dos caracteres
                    for cnt in self.contours:
                        x, y, w, h = cv2.boundingRect(cnt)
                        if(h > (self.height * 0.3) and w < (self.width * 0.2)):
                            self.contours_list.append(cnt)
                    # cria uma imagem branca e adiciona os contornos na imagem
                    self.blank_image = np.zeros((self.height,self.width,3), np.uint8)
                    cv2.drawContours(self.blank_image, self.contours_list, -1, (255,255,255), -1)
                    # converte a imagem para tons de cinza e procura os contornos
                    self.blank_image = cv2.cvtColor(self.blank_image, cv2.COLOR_BGR2GRAY)
                    self.contours, _ = cv2.findContours(self.blank_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    self.contours_sort = sorted(self.contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
                    self.result_character_image = np.zeros((self.height,10), np.uint8)
                    # obtem os contornos dos caracteres e uni os caracteres a uma unica imagem
                    for cnt in self.contours_sort:
                        x, y, w, h = cv2.boundingRect(cnt)
                        self.character_image = self.th2[y:y+h, x:x+w]
                        self.character_image = cv2.copyMakeBorder(self.character_image, (self.height - h - 20), 20, 10, 10, cv2.BORDER_CONSTANT, None, value = (255,255,255))
                        self.result_character_image = np.concatenate((self.result_character_image, self.character_image), axis=1)
                    # detecta o texto na imagem
                    self.plate_text = self.reader.readtext(self.result_character_image, detail = 0)
                    # uni o vetor de string em uma unica string
                    self.plate_text = ''.join(self.plate_text)
                    # verifica o tamanho da string para ve se a placa e valida
                    if(len(self.plate_text) == 7):
                        # converte a string para maiuscula
                        self.plate_text = self.plate_text.upper()

                        # altera os caracteres que podem ser confundidos
                        self.plate_text_1 = self.plate_text[:3]
                        self.plate_text_2 = self.plate_text[3]
                        self.plate_text_3 = self.plate_text[4]
                        self.plate_text_4 = self.plate_text[5:]

                        self.plate_text_1.replace('0', 'O')
                        self.plate_text_1.replace('1', 'I')
                        self.plate_text_1.replace('5', 'S')
                        self.plate_text_1.replace('7', 'Z')

                        self.plate_text_2.replace('O', '0')
                        self.plate_text_2.replace('I', '1')
                        self.plate_text_2.replace('S', '5')
                        self.plate_text_2.replace('?', '7')
                        self.plate_text_2.replace('Z', '7')

                        self.plate_text_3.replace('0', 'O')
                        self.plate_text_3.replace('1', 'I')
                        self.plate_text_3.replace('5', 'S')
                        self.plate_text_3.replace('7', 'Z')

                        self.plate_text_4.replace('O', '0')
                        self.plate_text_4.replace('I', '1')
                        self.plate_text_4.replace('S', '5')
                        self.plate_text_4.replace('?', '7')
                        self.plate_text_4.replace('Z', '7')

                        self.plate_text = self.plate_text_1 + self.plate_text_2 + self.plate_text_3 + self.plate_text_4
                        # obtem a imagem em uma proporcao menor
                        self.width_resize = int(self.img.shape[1] * 0.2)
                        self.height_resize = int(self.img.shape[0] * 0.2)
                        self.image_resize = cv2.resize(self.img, (self.width_resize, self.height_resize), interpolation = cv2.INTER_AREA)
                        # converte a imagem para base64
                        _, self.encode_pjg = cv2.imencode('.jpg', self.image_resize)
                        self.im_bytes = self.encode_pjg.tobytes()
                        self.jpg_as_text = base64.b64encode(self.im_bytes)
                        self.jpg_as_text = str(self.jpg_as_text)
                        self.jpg_as_text = self.jpg_as_text[2:-1]
                        # cria a query sql e insere os dados no banco de dados
                        self.sql = "INSERT INTO veiculo (placa, data, imagem) VALUES (%s, %s, %s)"
                        self.values = (self.plate_text, datetime.datetime.now(), self.jpg_as_text[1:])
                        self.cur.execute(self.sql, self.values)
                        self.con.commit()
        # fecha a conexao com o banco de dados
        self.cur.close()
        self.con.close()
# classe para executar o sistema        
class execute:
    def execute(video):
        Detection(video)

if (__name__ == "__main__"):
    execute().execute('video.mp4')

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
        def box_bounding(im, color=(114, 114, 114)):
            shape = im.shape[:2]
            ratio = min(640 / shape[0], 640 / shape[1])
            new_padding = int(round(shape[1] * ratio)), int(round(shape[0] * ratio))
            width, height = 640 - new_padding[0], 640 - new_padding[1]
            width /= 2 
            height /= 2
            if shape[::-1] != new_padding:
                im = cv2.resize(im, new_padding, interpolation=cv2.INTER_LINEAR)
            top, bottom = int(round(height - 0.1)), int(round(height + 0.1))
            left, right = int(round(width - 0.1)), int(round(width + 0.1))
            im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
            return im, ratio, (width, height)

        self.cap = cv2.VideoCapture(video)
        self.session = ort.InferenceSession("model_onnx/plate.onnx", providers=['CPUExecutionProvider'])
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.con = psycopg2.connect(host='localhost', database='cerbero', user='postgres', password='1234')
        self.cur = self.con.cursor()

        while self.cap.isOpened():
            _, self.img = self.cap.read()
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.image = self.img.copy()
            self.image, self.ratio, width_height = box_bounding(self.image)
            self.image = self.image.transpose((2, 0, 1))
            self.image = np.expand_dims(self.image, 0)
            self.image = np.ascontiguousarray(self.image)
            self.im = self.image.astype(np.float32)
            self.im /= 255
            self.outname = [i.name for i in self.session.get_outputs()]
            self.inname = [i.name for i in self.session.get_inputs()]
            self.inp = {self.inname[0]:self.im}
            self.outputs = self.session.run(self.outname, self.inp)[0]
            self.ori_images = [self.img.copy()]

            for i,(batch_id,x0,y0,x1,y1,cls_id,score) in enumerate(self.outputs):
                if(score > 0.9):
                    image = self.ori_images[int(batch_id)]
                    self.box = np.array([x0,y0,x1,y1])
                    self.box -= np.array(width_height*2)
                    self.box /= self.ratio
                    self.box = self.box.round().astype(np.int32).tolist()
                    self.plate = image[self.box[1]:self.box[3],self.box[0]:self.box[2]]
                    self.grayPlate = cv2.cvtColor(self.plate, cv2.COLOR_BGR2GRAY)
                    self.th2 = cv2.adaptiveThreshold(self.grayPlate,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,4)
                    self.height, _ = self.th2.shape[:2]
                    self.x = 318 / self.height
                    self.th2 = cv2.resize(self.th2, (0, 0), fx=self.x, fy=self.x, interpolation=cv2.INTER_AREA)
                    self.height, self.width = self.th2.shape[:2]
                    self.contours, _ = cv2.findContours(self.th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    self.contours_list = []
                    for cnt in self.contours:
                        x, y, w, h = cv2.boundingRect(cnt)
                        if(h > (self.height * 0.3) and w < (self.width * 0.2)):
                            self.contours_list.append(cnt)
                    self.blank_image = np.zeros((self.height,self.width,3), np.uint8)
                    cv2.drawContours(self.blank_image, self.contours_list, -1, (255,255,255), -1)
                    self.blank_image = cv2.cvtColor(self.blank_image, cv2.COLOR_BGR2GRAY)
                    self.contours, _ = cv2.findContours(self.blank_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    self.result_character_image = np.zeros((self.height,10), np.uint8)
                    for cnt in self.contours:
                        x, y, w, h = cv2.boundingRect(cnt)
                        self.character_image = self.th2[y:y+h, x:x+w]
                        self.character_image = cv2.copyMakeBorder(self.character_image, (self.height - h - 20), 20, 10, 10, cv2.BORDER_CONSTANT, None, value = (255,255,255))
                        self.result_character_image = np.concatenate((self.result_character_image, self.character_image), axis=1)
                    self.plate_text = self.reader.readtext(self.result_character_image, detail = 0)
                    self.plate_text = ''.join(self.plate_text)
                    if(len(self.plate_text) == 7):
                        self.width_resize = int(self.img.shape[1] * 0.2)
                        self.height_resize = int(self.img.shape[0] * 0.2)
                        self.image_resize = cv2.resize(self.img, (self.width_resize, self.height_resize), interpolation = cv2.INTER_AREA)
                        _, self.encode_pjg = cv2.imencode('.jpg', self.image_resize)
                        self.jpg_as_text = base64.b64encode(self.encode_pjg)
                        self.sql = "INSERT INTO veiculo (placa, data, imagem) VALUES (%s, %s, %s)"
                        self.values = (self.plate_text, datetime.datetime.now(), self.jpg_as_text[1:])
                        self.cur.execute(self.sql, self.values)
                        self.con.commit()
        self.cur.close()
        self.con.close()
        
class execute:
    def execute(video):
        Detection(video)

if (__name__ == "__main__"):
    execute().execute('video.mp4')

import cv2
import numpy as np
import onnxruntime as ort
import easyocr

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

img = cv2.imread('arquivos/image4.JPG')
session = ort.InferenceSession("plate.onnx", providers=['CPUExecutionProvider'])
reader = easyocr.Reader(['en'], gpu=False)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image = img.copy()
image, ratio, width_height = box_bounding(image)
image = image.transpose((2, 0, 1))
image = np.expand_dims(image, 0)
image = np.ascontiguousarray(image)
im = image.astype(np.float32)
im /= 255
outname = [i.name for i in session.get_outputs()]
inname = [i.name for i in session.get_inputs()]
inp = {inname[0]:im}
outputs = session.run(outname, inp)[0]
ori_images = [img.copy()]

for i,(batch_id,x0,y0,x1,y1,cls_id,score) in enumerate(outputs):
    if(score > 0.9):
        image = ori_images[int(batch_id)]
        box = np.array([x0,y0,x1,y1])
        box -= np.array(width_height*2)
        box /= ratio
        box = box.round().astype(np.int32).tolist()
        plate = image[box[1]:box[3],box[0]:box[2]]
        grayPlate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        th2 = cv2.adaptiveThreshold(grayPlate,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,4)
        height, _ = th2.shape[:2]
        x = 318 / height
        th2 = cv2.resize(th2, (0, 0), fx=x, fy=x, interpolation=cv2.INTER_AREA)
        height, width = th2.shape[:2]
        contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_list = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if(h > (height * 0.3) and w < (width * 0.2)):
                contours_list.append(cnt)
        blank_image = np.zeros((height,width,3), np.uint8)
        cv2.drawContours(blank_image, contours_list, -1, (255,255,255), -1)
        blank_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(blank_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        result_character_image = np.zeros((height,10), np.uint8)
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            character_image = th2[y:y+h, x:x+w]
            character_image = cv2.image = cv2.copyMakeBorder(character_image, (height - h - 20), 20, 10, 10, cv2.BORDER_CONSTANT, None, value = (255,255,255))
            result_character_image = np.concatenate((result_character_image, character_image), axis=1)
            result = reader.readtext(result_character_image, detail = 0)


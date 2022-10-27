from PIL import Image
import numpy as np
import onnxruntime as rt

MODEL = "plate.onnx"
IMAGE = 'image.JPG'

# inference session
img = Image.open(IMAGE)
img = img.resize((640, 640))
img_data = np.array(img.getdata()).reshape(3, img.size[1], img.size[0])
img_data = np.expand_dims(img_data.astype(np.float32), axis=0)
sess = rt.InferenceSession(MODEL, None, providers=['CPUExecutionProvider'])
outputs = ["output"]
result = sess.run(outputs, {'images': img_data})[0]

for i, (batch_id, x0, y0, x1, y1, cls_id, score) in enumerate(result):
    box = np.array([x0, y0, x1, y1])

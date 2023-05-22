# yolo object identify
import cv2
import numpy as np

classes = open('./yolo_file/coco.names').read().strip().split('\n')
np.random.seed(42)
colors = np.random.randint(0, 255, size = (len(classes), 3), dtype = 'uint8')

net = cv2.dnn.readNetFromDarknet('./yolo_file/yolov3.cfg', 
                                 './yolo_file/yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

# decide output layer
ln = net.getLayerNames()
ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

def post_process(img, outputs, conf):
    H, W = img.shape[ : 2]
    boxes = []
    confidences = []
    classIDs = []

    for output in outputs:
        scores = output[5 : ]
        classID = np.argmax(scores)
        confidence = scores[classID]

        if confidence > conf: 
            x, y, w, h = output[ : 4] * np.array([W, H, W, H])
            p0 = int(x - w//2), int(y - h//2)
            p1 = int(x + w//2), int(y + h//2)
            boxes.append([*p0, int(w), int(h)])
            confidences.append(float(confidence))
            classIDs.append(classID)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf, conf-0.1)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = "{} : {:.4f}".format(classes[classIDs[i]], confidences[i])
            cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

img0 = cv2.imread('./img/horse.jpg')
img = img0.copy()
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB = True, crop = False)

net.setInput(blob)
outputs = net.forward(ln)
outputs = np.vstack(outputs)
post_process(img, outputs, 0.5)
cv2.imshow('window', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
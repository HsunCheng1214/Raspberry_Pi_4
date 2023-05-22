# detect face from camera
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray_img,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30)
    )

    print("faces: ", len(faces))

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("preview", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  

cap.release()
cv2.destroyAllWindows()
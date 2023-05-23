#face mesh
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector()

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, 0)
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
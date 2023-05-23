# Hands: How many fingers
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon = 0.5, maxHands = 2)

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, -1)
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}',
                   (bbox[0]+200, bbox[1]-30),
                   cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
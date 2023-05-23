# Hands detect
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
        hand1 = hands[0]
        lmList = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]
        finger1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2['center']
            handType2 = hand2["type"]
            finger2 = detector.fingersUp(hand2)
            length, info, img = detector.findDistance(lmList[8], lmList2[8], img)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
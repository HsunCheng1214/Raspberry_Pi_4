# fingers removing
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=2)

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, -1)
    hands, img = detector.findHands(img)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)        
        length, info, img = detector.findDistance(lmList1[8],lmList1[12],img)
        cv2.putText(img, f'Dist:{int(length)}',(bbox1[0]+100,bbox1[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)        
        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2['center']
            handType2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            length, info, img = detector.findDistance(lmList1[8],lmList2[8],img)
            cv2.putText(img, f'Dist:{int(length)}',(bbox2[0]+100,bbox2[1]-30),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
#set picture size
import cv2
import imutils

img = cv2.imread("./img/squirrel.jpg")

resized_img = imutils.resize(img, width=500)

cv2.imshow("squirrel", img)
cv2.imshow("squirrel:gray", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

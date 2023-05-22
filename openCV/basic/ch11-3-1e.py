#BGR gray
import cv2

img = cv2.imread("./img/squirrel.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("squirrel", img)
cv2.imshow("squirrel:gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
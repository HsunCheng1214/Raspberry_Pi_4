#picture show on
import cv2

img = cv2.imread("./img/squirrel.jpg")
cv2.imshow("squirrel", img)

gray_img = cv2.imread("./img/squirrel.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("squirrel:gray", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
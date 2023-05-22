#crop picture
import cv2

img = cv2.imread("./img/squirrel.jpg")

x = 10
y = 10
w = 150 
h = 200
crop_img = img[y:y+h, x:x+w]

cv2.imshow("squirrel", img)
cv2.imshow("squirrel:crop", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
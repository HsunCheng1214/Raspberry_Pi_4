#rotated, fliped, translated
import cv2
import imutils

img = cv2.imread("./img/squirrel.jpg")
rotated_img = imutils.rotate(img, angle=90)
fliped_img = cv2.flip(img, -1)
translated_img = imutils.translate(img, 25, -75)


cv2.imshow("squirrel", img)
cv2.imshow("rotated_img", rotated_img)
cv2.imshow("fliped_img", fliped_img)
cv2.imshow("translated_img", translated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
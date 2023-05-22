#get picture from URL
import cv2
import imutils

url = "http://fchart.github.io/img/koala.png"
img = imutils.url_to_image(url)

cv2.imshow("koala", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
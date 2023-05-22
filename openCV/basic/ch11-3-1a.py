#picture information 
import cv2

img = cv2.imread("./img/squirrel.jpg")
img2 = cv2.imread("./img/squirrel.jpg", cv2.IMREAD_GRAYSCALE)

print(img.shape)
print(img2.shape)

h, w, c = img.shape

print("imager height: ", h)
print("imager width: ", w)
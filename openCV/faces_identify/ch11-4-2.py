# detect face from image
import cv2
import imutils

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("./img/faces.jpg")
#image = imutils.resize(image, height = 553)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

h, w, c = image.shape
print("image height: ", h)
print("image width: ", w)

#from picture detect face
faces = faceCascade.detectMultiScale(
    gray_img,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30, 30)
)   

print("faces: ", len(faces))

for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #          coordinate start,     end,       color,   line width     

cv2.imshow("preview", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
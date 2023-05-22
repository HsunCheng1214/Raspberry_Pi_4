# show video information
import cv2

cap = cv2.VideoCapture('./video/YouTube.mp4')

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * 1) & 0xFF) for i in range(4)])

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("image size: ", width, "x", height)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
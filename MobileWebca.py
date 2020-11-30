import cv2


URL = "http://192.168.43.123:8080"
cam = cv2.VideoCapture(URL)

while True:
    check, img = cam.read()
    cv2.imshow('IPWebcam', img)
    height, width, channels = img.shape
    print(height, width, channels)
    if cv2.waitKey(1) == 27:
      break

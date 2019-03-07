import cv2
import numpy
import time

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()
start_clock = time.clock()


while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 300:
        img_name = "FaceFrame{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_counter))
        start_time = time.time()
    img_counter += 1

    if (time.clock() - start_clock) > 21600:
        break
    

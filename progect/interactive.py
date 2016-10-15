import cv2
import sys
import numpy as np

THRESHOLD = 20
MORPHOLOGIC_OPERATION_SIZE = (2,2)
CONTOUR_EPS = 1

video_capture = cv2.VideoCapture(0)

ret, average_frame = video_capture.read()
average_frame = cv2.cvtColor(average_frame, cv2.COLOR_BGR2GRAY)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    binary = cv2.threshold(cv2.absdiff(average_frame, gray_frame), THRESHOLD,255,cv2.THRESH_BINARY)[1]
    binary = cv2.erode(binary, np.ones(MORPHOLOGIC_OPERATION_SIZE))
    binary = cv2.dilate(binary, np.ones(MORPHOLOGIC_OPERATION_SIZE))

    binary2 = binary.copy()
    frame2 = frame.copy()
    im2, contours, hierarchy = cv2.findContours(binary2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,CONTOUR_EPS,True)
        cv2.polylines(frame2,cnt,True,(0,255,255))

    cv2.imshow('Video', binary2)
    cv2.imshow('Video2', frame2)


    average_frame = average_frame//2 + gray_frame//2
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
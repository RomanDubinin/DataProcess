import cv2
import sys
import numpy as np

class MovingProvider():
    def __init__(self, average_frame):
        self.average_frame = average_frame

    def get_moved_contours(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        binary = cv2.threshold(cv2.absdiff(self.average_frame, gray_frame), THRESHOLD,255,cv2.THRESH_BINARY)[1]
        binary = cv2.erode(binary, np.ones(MORPHOLOGIC_OPERATION_SIZE))
        binary = cv2.dilate(binary, np.ones(MORPHOLOGIC_OPERATION_SIZE))

        cv2.imshow('Video', binary)

        im2, contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

        self.average_frame = self.average_frame//2 + gray_frame//2

        return contours



THRESHOLD = 20
MORPHOLOGIC_OPERATION_SIZE = (2,2)
CONTOUR_EPS = 1

video_capture = cv2.VideoCapture(0)

ret, average_frame = video_capture.read()
average_frame = cv2.cvtColor(average_frame, cv2.COLOR_BGR2GRAY)
moving_provider = MovingProvider(average_frame)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()



    contours = moving_provider.get_moved_contours(frame)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,CONTOUR_EPS,True)
        cv2.polylines(frame,cnt,True,(0,255,255))


    cv2.imshow('Video2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
import cv2
import sys
import numpy as np
import random
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point (self.x + other.x, self.y + other.y)

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


def get_random_vector(min_len, max_len):
    length = random.randint(min_len, max_len)
    angle  = random.random() * math.pi * 2

    return Point(length * math.cos(angle), length * math.sin(angle))


THRESHOLD = 20
MORPHOLOGIC_OPERATION_SIZE = (2,2)
CONTOUR_EPS = 1

video_capture = cv2.VideoCapture(0)

ret, average_frame = video_capture.read()
average_frame = cv2.cvtColor(average_frame, cv2.COLOR_BGR2GRAY)
moving_provider = MovingProvider(average_frame)

HEIGTH, WIDTH = average_frame.shape
CENTER = Point(WIDTH//2,HEIGTH//2)
base_pos = CENTER

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()



    contours = moving_provider.get_moved_contours(frame)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,CONTOUR_EPS,True)
        cv2.polylines(frame,cnt,True,(0,255,255))


    base_pos = get_random_vector(0, 10) + base_pos
    cv2.circle(frame, (int(base_pos.x), int(base_pos.y)), 13, (255,0,0), thickness=-1)
    cv2.imshow('Video2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
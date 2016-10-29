import cv2
import sys
import numpy as np
import random
import math
from Vector import Vector
from MovingProvider import MovingProvider
from Base import Base
import Constants

def get_random_vector(min_len, max_len):
    length = random.randint(min_len, max_len)
    angle  = random.random() * math.pi * 2

    return Vector(length * math.cos(angle), length * math.sin(angle))

video_capture = cv2.VideoCapture(0)

ret, average_frame = video_capture.read()
average_frame = cv2.cvtColor(average_frame, cv2.COLOR_BGR2GRAY)
moving_provider = MovingProvider(average_frame)

HEIGTH, WIDTH = average_frame.shape
CENTER = Vector(WIDTH//2,HEIGTH//2)
base = Base(CENTER, CENTER, WIDTH//2, HEIGTH//2)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    contours = moving_provider.get_moved_contours(frame)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, Constants.CONTOUR_EPS,True)
        cv2.polylines(frame,cnt,True,(0,255,255))


    base.move_by(get_random_vector(0, 10))
    cv2.circle(frame, (int(base.position.x), int(base.position.y)), 13, (255,0,0), thickness=-1)
    cv2.imshow('Video2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
import cv2
import Constants
import numpy as np

class MovingProvider():
    def __init__(self, average_frame):
        self.average_frame = average_frame

    def get_moved_contours(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        binary = cv2.threshold(cv2.absdiff(self.average_frame, gray_frame), Constants.THRESHOLD,255,cv2.THRESH_BINARY)[1]
        binary = cv2.erode(binary, np.ones(Constants.MORPHOLOGIC_OPERATION_SIZE))
        binary = cv2.dilate(binary, np.ones(Constants.MORPHOLOGIC_OPERATION_SIZE))

        cv2.imshow('Video', binary)

        im2, contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

        self.average_frame = self.average_frame//2 + gray_frame//2

        return contours
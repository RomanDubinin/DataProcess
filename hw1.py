import numpy as np
import cv2

# Load an color image in grayscale
image = cv2.imread('1.jpg')

b,g,r = cv2.split(image)

_, thresholded_b = cv2.threshold(b, 100, 255, cv2.THRESH_BINARY)


cropped_copy = image[100:500, 100: 500].copy()

image2 = image
image2[100:500, 100: 500] = image[100:500, 100: 500] * 0.6

#cv2.imshow('crop',cropped_copy)
#cv2.imshow('image2',thresholded_b)
cv2.imshow('image',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
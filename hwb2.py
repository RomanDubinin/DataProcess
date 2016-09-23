import cv2
import sys
import numpy as np

video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,100,100])
    upper_blue = np.array([130,255,255])

    binary = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    
    im2, contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if (w + h > 50):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
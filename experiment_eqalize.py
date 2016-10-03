import numpy as np
import cv2

def eqalize(channel):
	height, width = channel.shape[:2]
	hist = [0] * height * width
	print(len(hist))
	print(height, width)
	for x in range(width):
		for y in range(height):
			hist[channel[y, x]] += 1

	for i in range(1, len(hist)):
		hist[i] = hist[i] + hist[i-1]

	new_brightnes = [0] * 256
	for i in range(256):
		new_brightnes[i] = min( int(256 * hist[i] / len(hist)) , 255)

	for x in range(width):
		for y in range(height):
			channel[y, x] = new_brightnes[channel[y, x]]
	return channel
			

# Load an color image in grayscale
image = cv2.imread('18510029_2_500.JPG')
print(image[0, 0])
b,g,r = cv2.split(image)

new_b = eqalize(b)
new_g = eqalize(g)
new_r = eqalize(r)

new_image = cv2.merge((new_b,new_g,new_r))

cv2.imwrite("18510029_2_500_eq.JPG", new_image)

imS = cv2.resize(image, (760, 540))                    # Resize image
cv2.imshow("output1", imS)


imS = cv2.resize(new_image, (760, 540))                    # Resize image
cv2.imshow("output2", imS)



cv2.waitKey(0)
cv2.destroyAllWindows()
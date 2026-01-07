import cv2
import numpy as nm

from utils.common import IMAGE_FOLDER_PATH

image = cv2.imread(IMAGE_FOLDER_PATH + "jack_jones.png")
if image is None:
    print("Couldn't load image!!")
    exit(0)

# image is numpy ndarray type
print(f"Image type: {type(image)}")
print(f"Image pixel: {image[1, 1]}")

# color to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("jack_jones_gray", gray)

# access image pixel value
B, G, R = image[100, 100]
print(f"Color of color image: B = {B} G = {G} R = {R}")
print(f"Color of gray image: {gray[100, 100]}")

# draw a white square
image[50:80, 50:150] = [255, 255, 255]
cv2.imshow("jj_square", image)

# brighter image
image_brighter = image + 50
cv2.imshow("jj_brighter", image_brighter)

cv2.waitKey(0)
cv2.destroyAllWindows()



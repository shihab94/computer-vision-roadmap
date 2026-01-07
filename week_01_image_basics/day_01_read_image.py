import cv2 as cv

from utils.common import IMAGE_FOLDER_PATH

# read image
image = cv.imread(IMAGE_FOLDER_PATH+'jack_jones.png')

if image is None :
   print("No image found")
   exit(0)

# show image
cv.imshow('jack_jones', image)

# printing details
print(image.shape)
print(image.dtype)

# convert image to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('jack_jones_grayscale', gray_image)

# printing grayscale image details
print(gray_image.shape)
print(gray_image.dtype)

# displaying red dot in color image
image[400, 250] = (0, 0, 255)
cv.imshow('jack_jones_grayscale_red_dot', image)

# displaying read circle in grayscale image
cv.circle(gray_image, (400,250), 10, (0,0,255), -1)
cv.imshow('jack_jones_grayscale_red_circle', gray_image)

cv.waitKey(0)

cv.destroyAllWindows()
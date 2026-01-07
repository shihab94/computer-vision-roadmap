import cv2

from utils.common import IMAGE_FOLDER_PATH

# read image
image = cv2.imread(IMAGE_FOLDER_PATH + 'jack_jones.png')

if image is None :
    print("Couldn't load the image.")
    exit(0)

# fixed resize
fixed_resize_image = cv2.resize(image, (350, 350))
cv2.imshow("fixed_size_img", fixed_resize_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

# create a gray background image
img_arr = np.zeros((250, 250), np.uint8)
img_arr[:, :] = 80

# create a white square inside the gray square
img_arr[70:200, 70:120] = 255

cv2.imshow("gray_square", img_arr)

cv2.waitKey(0)
cv2.destroyAllWindows()
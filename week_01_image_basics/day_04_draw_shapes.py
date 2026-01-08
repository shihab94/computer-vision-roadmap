import cv2

from utils.common import IMAGE_FOLDER_PATH

# load image
image = cv2.imread(IMAGE_FOLDER_PATH + "jack_jones.png")

if image is None:
    print("Couldn't load image!!")
    exit(0)

# copy image
img = image.copy()

# draw line
cv2.line(img, (0, 0), (300, 50), (0, 0, 255), 1)

# draw rectangle
cv2.rectangle(img, (300, 100), (350,150), (0, 0, 255), 2)

# draw circle
cv2.circle(img, (300, 300), 50, (0, 255, 0), -1)

# write text
cv2.putText(img, "Object", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("jj_line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
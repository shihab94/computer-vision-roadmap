import cv2
import numpy as np
import math
from datetime import datetime

def draw_hand(img, angle, length, color, thickness):
    angle = math.radians(angle)
    x = int(center[0] + math.cos(angle) * length)
    y = int(center[1] + math.sin(angle) * length)
    cv2.line(img, center, (x, y), color, thickness)

size = 500
img = np.zeros((size, size, 3), dtype=np.uint8)

center = (size // 2, size // 2)
radius = 200

cv2.circle(img, center, radius, (255, 255, 255), 2)
cv2.circle(img, center, 5, (255, 255, 255), -1)


while True:
    img = np.zeros((size, size, 3), dtype=np.uint8)

    cv2.circle(img, center, radius, (255, 255, 255), 2)
    cv2.circle(img, center, 5, (255, 255, 255), -1)

    for hour_num in range(1, 13):
        angle = math.radians((hour_num * 30) - 90)
        x = int(center[0] + math.cos(angle) * 170)
        y = int(center[1] + math.sin(angle) * 170)
        cv2.putText(img, str(hour_num), (x - 10, y + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    second_angle = (second * 6) - 90
    minute_angle = (minute * 6) - 90
    hour_angle = (hour * 30 + minute * 0.5) - 90

    draw_hand(img, hour_angle, 100, (255,255,255), 6)
    draw_hand(img, minute_angle, 150, (255,255,255), 4)
    draw_hand(img, second_angle, 180, (0,0,255), 2)

    cv2.imshow("Analog Clock", img)

    if cv2.waitKey(1) == 27:  # ESC key
        break

cv2.destroyAllWindows()

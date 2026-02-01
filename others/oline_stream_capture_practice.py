import cv2

source_url = "rtsp://192.168.23.11:1945"

capture = cv2.VideoCapture(source_url)

while True :

    ret, frame = capture.read()

    if not ret :
        print(f"Return is {ret}")
        break

    cv2.imshow("Online Stream", frame)

    if cv2.waitKey(1) and 0xFF == ord('q') :
        print("Program terminated!!")
        break

capture.release()
cv2.destroyAllWindows()

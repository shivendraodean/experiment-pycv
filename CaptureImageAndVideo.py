import cv2

print("hello pck imported")

# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output", img)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# cap = cv2.VideoCapture("Resources/flowergirl.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
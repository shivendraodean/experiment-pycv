import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

kernal = np.ones((5,5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7,7),0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernal, iterations=1)
imgEroded = cv2.erode(imgDialation, kernal, iterations=1)

cv2.imshow("Canny img", imgCanny)
cv2.imshow("Dialated Image", imgDialation)
cv2.imshow("ErodedImage", imgEroded)

cv2.waitKey(0)
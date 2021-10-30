import cv2
import numpy as np
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# img[200:300, 100:300] = 255,0,0

#line
cv2.line(img, (0,0), (300,300), (0,255,0), 3)

# rectangle
cv2.rectangle(img, (100,200), (400, 300), (0, 0, 255), 2)

# filled rectangle
cv2.rectangle(img, (450,470), (500, 500), (255, 0, 0), cv2.FILLED)

# circle
cv2.circle(img, (400, 50), (30), (255,255,0), 5)

#text
cv2.putText(img, "Hello Shiv ", (300, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150,0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
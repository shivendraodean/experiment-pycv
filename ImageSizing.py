import cv2

img = cv2.imread("Resources/lena.png")
cv2.imshow("Default Image", img)

# Get shape/dimensions
print(img.shape)

# Resize
imgResized = cv2.resize(img, (300, 200))
cv2.imshow("Resized", imgResized)

# Crop
imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)
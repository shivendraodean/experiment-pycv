import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

print("hello pck imported")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


while True:
    success, img = cap.read()
    imgResult = img.copy()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.imwrite('Resources/outputx.png', imgResult)
        break

    faces = faceCascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        print(faces)
        cv2.rectangle(imgResult, (x, y), (x + w, y + h), (255, 225, 0), 1)

    cv2.imshow("Facerrr", imgResult)


cv2.waitKey(0)
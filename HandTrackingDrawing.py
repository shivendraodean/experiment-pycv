import cv2
import numpy as np
import mediapipe as mp
import time

canvas = np.zeros((1080, 1920, 3), np.uint8)

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(10, 100)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 8:
                    cv2.circle(canvas, (1920-cx, cy), 25, (255,0,255), cv2.FILLED)

    cv2.imshow("Tracker Canvas", canvas)
    cv2.waitKey(1)
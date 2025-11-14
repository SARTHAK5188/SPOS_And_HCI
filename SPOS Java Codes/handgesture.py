# Requirements:
# pip install opencv-python mediapipe
#
# How to run:
# 1. Save this file as gesture.py
# 2. Ensure your webcam is connected and not used by another app.
# 3. Run: python gesture.py
# 4. Press 'q' in the window to quit.
#
# (Only the necessary instructions above - no extra text inside the code.)

import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
# set detection/tracking confidence for more stable results
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

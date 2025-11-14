# FaceRecognition.py
# ------------------
# Requirements:
#   - Python 3.8+
#   - Install required library:
#       pip install opencv-python
#
# Quick steps to run:
#   1. (Optional) create & activate a virtual environment.
#   2. Install dependency: pip install opencv-python
#   3. Connect a webcam (or ensure your laptop camera is available).
#   4. Run: python FaceRecognition.py
#   5. Window shows live video; press 'q' to quit.
#
# Notes:
#   - If your camera is not at index 0, change VideoCapture(0) to another index (1,2,...).
#   - If the program crashes on reading frames, check camera permissions / device drivers.
#   - This script uses OpenCV's Haar cascade bundled in the package.

import cv2
import sys

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("ERROR: Failed to load Haar cascade. Check your OpenCV installation.")
    sys.exit(1)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Cannot open camera. Check camera index and permissions.")
    sys.exit(1)

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        # skip this iteration if frame not read properly
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

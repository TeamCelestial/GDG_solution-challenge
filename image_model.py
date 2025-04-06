# image_model.py - MediaPipe for Image Detection

import mediapipe as mp
import cv2

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detect_faces(image):
    with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
        results = face_detection.process(image)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
        return image

# backend/models/image_model.py
def detect_faces(image_data):
    return "Fake image detection result"

import cv2 
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


def analyze_pose(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        return results.pose_landmarks.landmark
    return None
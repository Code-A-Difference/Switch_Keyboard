import cv2
import pyautogui
import time
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.face_detection as mp_face
import mediapipe.python.solutions.drawing_utils as mp_drawing

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
face_detection = mp_face.FaceDetection(min_detection_confidence=0.6)

cap = cv2.VideoCapture(0)
cooldown_timer = 0
COOLDOWN_DELAY = 1.0

print("🚀 Unified Classroom Switcher App Active!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_results = face_detection.process(rgb_frame)
    hand_results = hands.process(rgb_frame)
    
    nose_y = None
    wrist_y = None

    if face_results.detections:
        for detection in face_results.detections:
            relative_keypoints = detection.location_data.relative_keypoints
            if relative_keypoints:
                nose_y = relative_keypoints[2].y * h
                cv2.line(frame, (0, int(nose_y)), (w, int(nose_y)), (255, 255, 0), 1)
                cv2.putText(frame, "Trigger Line", (10, int(nose_y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
            break

    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            wrist_landmark = hand_landmarks.landmark[0]
            wrist_y = wrist_landmark.y * h
            cv2.circle(frame, (int(wrist_landmark.x * w), int(wrist_y)), 8, (0, 0, 255), -1)

    current_time = time.time()
    if nose_y is not None and wrist_y is not None:
        if wrist_y < nose_y:
            if current_time > cooldown_timer:
                print("🎯 AI Confirmed: Hand Raised Above Nose Level!")
                pyautogui.press('space')
                cooldown_timer = current_time + COOLDOWN_DELAY
                cv2.rectangle(frame, (0, 0), (w, h), (0, 255, 0), 10)

    cv2.imshow('Classroom Hand Gesture Tracker', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

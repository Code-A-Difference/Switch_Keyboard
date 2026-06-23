import cv2
import pyautogui
import time
from collections import deque

# Load the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

# Fast-rolling history for instant acceleration calculations
movement_history = deque(maxlen=4)
last_y = None
cooldown_timer = 0

print("🚀 High-Speed Accessibility Engine Active!")
print("Frames are optimized. Small, quick nods will trigger instantly.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    
    # --- UPGRADE 1: DOWNSCALE FOR HIGHER FPS ---
    # Downscaling the image reduces computation dramatically, stripping out camera lag
    h_orig, w_orig = frame.shape[:2]
    target_w = 400
    scale_ratio = target_w / float(w_orig)
    target_h = int(h_orig * scale_ratio)
    
    small_frame = cv2.resize(frame, (target_w, target_h))
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # --- UPGRADE 2: LIGHTWEIGHT CASCADE SCAN ---
    # Fast scale factor to ensure the detector checks your position instantly
    faces = face_cascade.detectMultiScale(gray, 1.2, 3, minSize=(30, 30))

    if len(faces) > 0:
        # Sort to grab the largest face region found (closest user)
        (x, y, w, h) = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)[0]
        
        # Scale coordinates back up so the visual display window looks perfect
        cv2.rectangle(frame, (int(x/scale_ratio), int(y/scale_ratio)), 
                      (int((x+w)/scale_ratio), int((y+h)/scale_ratio)), (0, 255, 255), 2)
        
        center_y = y + (h // 2)

        if last_y is not None:
            # Scale-independent downward velocity measurement
            instant_velocity = (center_y - last_y) / float(h)
            movement_history.append(instant_velocity)
            
            # Accumulate positive downward trends
            downward_momentum = sum([v for v in movement_history if v > 0])

            # --- UPGRADE 3: ULTRA-SENSITIVE THRESHOLD ---
            # Dropped to 0.025 to catch subtle facial tilts instantly
            if downward_momentum > 0.025 and time.time() > cooldown_timer:
                print(f"💥 Instant Switch Activated! (Momentum: {round(downward_momentum, 3)})")
                pyautogui.press('space')
                
                # Snappy 0.35s delay lets you type at a fast, regular rhythm
                cooldown_timer = time.time() + 0.35
                movement_history.clear()

        last_y = center_y
    else:
        # If a fast nod temporarily breaks face tracking, slowly decay the history 
        # instead of losing track of your position entirely
        if len(movement_history) > 0:
            movement_history.popleft()

    # Display full resolution feed for clean user monitoring
    cv2.imshow('High-Speed Responsive Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
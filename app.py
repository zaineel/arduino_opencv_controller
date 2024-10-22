import cv2
import mediapipe as mp
import time
import controller as ctrl

time.sleep(2.0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

tip_ids = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = video.read()
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        if len(lmList) != 0:
            fingers = []
            # Thumb
            if lmList[tip_ids[0]][1] > lmList[tip_ids[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # 4 Fingers
            for id in range(1, 5):
                if lmList[tip_ids[id]][2] < lmList[tip_ids[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            totalFingers = fingers.count(1)
            ctrl.turn_on_led(totalFingers)
            cv2.putText(frame, f'Fingers: {totalFingers}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.imshow('Hand Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()




import cv2
import mediapipe as mp
import math
import numpy as np

class Button:
    def _init_(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        overlay = img.copy()
        cv2.rectangle(overlay, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (250, 251, 217), cv2.FILLED)
        alpha = 0.4
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    def checkClick(self, x, y):
        return (self.pos[0] < x < self.pos[0] + self.width and
                self.pos[1] < y < self.pos[1] + self.height)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

buttonListValue = [["C", "", "", ""],
                   ["1", "2", "3", "+"],
                   ["4", "5", "6", "-"],
                   ["7", "8", "9", "*"],
                   ["0", "/", ".", "="]]

buttonList = []
for x in range(4):
    for y in range(5):
        xPos = x * 70 + 350
        yPos = y * 70 + 100
        if y == 0 and x == 0:
            xPos = 10
            yPos = 10
        buttonList.append(Button((xPos, yPos), 70, 70, buttonListValue[y][x]))

equation = ""
history = []
delayCounter = 0

def save_result_to_file(result):
    with open("results.txt", "a") as f:
        f.write(f"{result}\n")

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    overlay = img.copy()

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            h, w, _ = img.shape
            index_finger_x, index_finger_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            distance = calculate_distance(index_finger_x, index_finger_y, thumb_x, thumb_y)
            pinch_threshold = 30

            if distance < pinch_threshold:
                for button in buttonList:
                    if button.checkClick(index_finger_x, index_finger_y) and delayCounter == 0:
                        if button.value == "=":
                            try:
                                result = str(eval(equation))
                                history.append(f"{equation} = {result}")
                                save_result_to_file(f"{equation} = {result}")
                                equation = result
                            except Exception:
                                equation = "Error"
                        elif button.value == "C":
                            equation = ""
                            history.clear()
                        else:
                            equation += button.value
                            history.append(button.value)
                        delayCounter = 1

    for button in buttonList:
        button.draw(overlay)

    alpha = 0.5
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
    cv2.rectangle(img, (350, 30), (350 + 280, 100), (250, 251, 217), cv2.FILLED)
    cv2.rectangle(img, (350, 30), (350 + 280, 100), (50, 50, 50), 3)
    cv2.putText(img, equation, (355, 80), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    history_text = "History: " + " ".join(history)
    history_pos = (10, 110)
    cv2.putText(img, history_text, history_pos, cv2.FONT_HERSHEY_PLAIN, 1, (50, 50, 50), 2)
    cv2.imshow("image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2

# Button class to set the borders and values inside the borders
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (250, 251, 217), cv2.FILLED)  # background
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)  # border
        cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)  # value

    def checkClick(self, x, y):
        if (self.pos[0] < x < self.pos[0] + self.width and
                self.pos[1] < y < self.pos[1] + self.height):
            return True
        return False

# Initialize camera
cap = cv2.VideoCapture(0)

# Creating buttons
buttonListValue = [["1", "2", "3", "+"],
                   ["4", "5", "6", "-"],
                   ["7", "8", "9", "*"],
                   ["0", "/", ".", "="]]
buttonList = []
for x in range(4):
    for y in range(4):
        xPos = x * 70 + 350  # starting from 350 pixels in width
        yPos = y * 70 + 100  # starting from 100 pixels in height
        buttonList.append(Button((xPos, yPos), 70, 70, buttonListValue[y][x]))

# Store the whole equation from the calculator
equation = ""
delayCounter = 0

# Mouse callback function to handle clicks
def click_event(event, x, y, flags, param):
    global equation, delayCounter
    if event == cv2.EVENT_LBUTTONDOWN:  # Check for left mouse button clicks
        for button in buttonList:
            if button.checkClick(x, y) and delayCounter == 0:
                if button.value == "=":
                    try:
                        equation = str(eval(equation))  # Evaluate the equation
                    except Exception as e:
                        equation = "Error"  # Handle any evaluation errors
                else:
                    equation += button.value
                delayCounter = 1

# Set mouse callback
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_event)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Draw the result display area
    cv2.rectangle(img, (350, 30), (350 + 280, 100), (250, 251, 217), cv2.FILLED)
    cv2.rectangle(img, (350, 30), (350 + 280, 100), (50, 50, 50), 3)

    # Draw buttons
    for button in buttonList:
        button.draw(img)

    # Avoid duplicates
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:  # Reset after 10 frames
            delayCounter = 0

    # Display the equation
    cv2.putText(img, equation, (355, 80), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
    cv2.imshow("image", img)

    key = cv2.waitKey(1)
    if key == ord("c"):  # Clear the display
        equation = ""
    if key == ord('q'):  # Stop the program
        break

cap.release()
cv2.destroyAllWindows()

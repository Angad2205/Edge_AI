import cv2  # Import the OpenCV library for computer vision tasks

#file_path = '1.png'

#img = cv.imread(file_path)

##cv.imshow('stop sign' , capture) 


# Create a VideoCapture object to access the default camera (index 0)
cap = cv2.VideoCapture(0)  

# Comment explaining that we will continuously capture and display frames from the webcam
# This will run an infinite loop until a specific condition is met
while True:
    # Capture a single frame from the webcam
    ret, frame = cap.read()  
    
    # Check if the frame was read successfully
    # 'ret' is True if the frame was read correctly, otherwise False
    # 'frame' is a NumPy array containing the image data of the captured frame
    if not ret:
        print("Failed to capture image")
        break
    
    # Print the raw pixel data of the frame to the console
    # 'frame' is a 3D NumPy array with shape (height, width, 3) for color images
    # Each pixel is represented by three values: Blue, Green, and Red in BGR format
    print(f"frame value is :{frame}")
    
    # Display the captured frame in a window named 'motion detection'
    # 'cv2.imshow()' takes the window name and the image data (frame) to be shown
    cv2.imshow('motion detection', frame)
    
    # Wait for a key press event for 1 millisecond
    # If the 'r' key is pressed, its ASCII code will match ord('r')
    if cv2.waitKey(1) == ord('r'):
        # Break out of the loop if 'r' key is pressed as cv.waitKey function wait for 1 mill second and check for any key which is pressed and convert it to the skiII value 
        break

# Release the webcam resource so it can be used by other applications
cap.release()

# Close all OpenCV windows that were opened during execution
cv2.destroyAllWindows()


import cv2
import numpy as np

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier("har_cascade.xml")
cap = cv2.VideoCapture(0)

while (1):
    # Capture frame from webcam
    _, frame = cap.read()
    
    # Convert the frame to grayscale for face detection
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=6)
    
    # Load the image for overlay (both with and without alpha)
    ka = cv2.imread("apple.webp", cv2.IMREAD_UNCHANGED)  # Try to load with transparency
    k = cv2.imread("apple.webp")  # Load normal RGB
    
    # Check if the image with alpha is loaded and has the correct number of channels
    if ka is None or len(ka.shape) < 3 or ka.shape[2] != 4:
        print("Image does not have an alpha channel or failed to load. Proceeding with RGB.")
        ka = None  # Set to None if alpha is not available

    # Process each detected face
    for face in detections:
        x, y, w, h = face
        
        # Resize the image overlay to fit on the detected face
        k1 = cv2.resize(k, (w // 3, h // 3))  # Resize the RGB image
        if ka is not None:
            ka1 = cv2.resize(ka, (w // 3, h // 3))  # Resize the RGBA image
        
        # Determine where to place the overlay on the face
        sy = y + h // 2 - h // 6
        sx = x + w // 2 - w // 6

        # If we have an alpha channel, apply it
        if ka is not None:
            # Apply the alpha channel as a mask on the RGB channels
            for c in range(3):  # For each channel (R, G, B)
                k1[:, :, c] = cv2.bitwise_and(k1[:, :, c], ka1[:, :, 3])

        # Extract the region of interest from the frame where the overlay will be placed
        fa = frame[sy:sy + h // 3, sx:sx + w // 3, :]
        
        # Combine the overlay and the region of interest using bitwise OR
        k1m = cv2.bitwise_or(k1, fa)
        
        # Place the modified region back into the frame if face position is valid
        if y > 100:
            frame[sy:sy + h // 3, sx:sx + w // 3] = k1m

    # Display the updated frame with the overlay
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the display window
cap.release()
cv2.destroyAllWindows()

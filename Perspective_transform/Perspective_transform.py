import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# Load the image
image_path = 'sample.jpeg'  # Ensure the path is correct or change to 'WhatsApp Image 2024-10-03 at 09.52.00_6e54a229.jpg'
if not os.path.exists(image_path):
    print(f"Error: {image_path} not found. Please check the file path.")
else:
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image file {image_path}.")
    else:
        # Get image dimensions
        rows, cols, ch = img.shape

        # Convert BGR to RGB for displaying with Matplotlib
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Display the image for point selection
        plt.imshow(img_rgb)
        plt.title('Select 4 points: Top-Left, Top-Right, Bottom-Left, Bottom-Right')
        x = plt.ginput(4)  # Manually select four points
        print(f"Selected Points: {x}")
        plt.show()

        if len(x) == 4:
            # Points for perspective transform
            # Ensure these points correspond to the correct corners in your image
            pts1 = np.float32([x[0], x[1], x[2], x[3]])  # Selected points (in the same order)
            pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])  # Target points for a rectangular output

            # Get the perspective transform matrix
            M = cv2.getPerspectiveTransform(pts1, pts2)

            # Apply perspective warp
            dst = cv2.warpPerspective(img, M, (cols, rows))

            # Convert the output image to RGB for display
            dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

            # Plot the input and output images
            plt.subplot(121), plt.imshow(img_rgb), plt.title('Input')
            plt.subplot(122), plt.imshow(dst_rgb), plt.title('Output')
            plt.show()
        else:
            print("Error: Please select exactly 4 points.")

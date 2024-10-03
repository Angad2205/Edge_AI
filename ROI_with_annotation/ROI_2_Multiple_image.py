import cv2 as cv
import os 

color = (0, 0, 255)
thickness = 1
scale = 1
font = cv.FONT_HERSHEY_COMPLEX
image_fol = 'images'
annotation_fol = 'annotation'
imlist = os.listdir(image_fol)

for im in imlist:
    img = cv.imread(os.path.join(image_fol, im))
    #this function is use to combine two path at the run time so that we can access multiple file of 
    # a folder at same time only
    #  cv.listdir ---> list the list of images in the folder 
    # os.path.join ---> join the path of folder and image with iteration so that all photo
    # can be access
    img = cv.resize(img, (450, 500))
    
    # Annotate the image
    org = (0, 50)
    img = cv.putText(img, "next", org, font, scale, color, thickness, cv.LINE_AA)
    org = (0, 450)
    img = cv.putText(img, "person", org, font, scale, color, thickness, cv.LINE_AA)
    org = (350, 450)
    img = cv.putText(img, "car", org, font, scale, color, thickness, cv.LINE_AA)

    # rename the file 
    frame = im[:-4]
    new_file = frame + '.txt'
    
    with open(os.path.join(annotation_fol, new_file), 'a') as f:
        while True:
            r = cv.selectROI(img)
            if r[0] < 70 and r[1] < 70:  # Exit condition
                break
            
            # Initialize 's' before checking conditions
            s = ''
            if r[1] > 450:
                if r[0] < 70:
                    s = 'person'
                elif 350 < r[0] < 400:
                    s = 'car'
            
            if s:  # Only write if 's' has been set
                line = f"{s} {r[0]} {r[1]} {r[2]} {r[3]}\n"
                f.write(line)
    f.close(f)
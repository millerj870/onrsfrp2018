# ACTION:
# captures video from laptop camera, grabs each frame and computes the Canny images in the frame; 
# displays the images of the edges in a window; 
# type "q" to quit

import numpy as np
import cv2
#from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

i=0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,180,220,5)

    # create a 4-character index
    j=str(i).zfill(3)
    cv2.imwrite("frame"+j+".PNG",edges)
    # Display the resulting frame
    cv2.imshow('frame',edges)
    i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
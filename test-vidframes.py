# ACTION:
# captures video from laptop camera and displays as greyscale in window; 
# type "q" to quit

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

i=0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    # create a 4-character index
    j=str(i).zfill(3)
    cv2.imwrite("frame"+j+".PNG",gray)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
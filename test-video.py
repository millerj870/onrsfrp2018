# ACTION:
# open saved movie, convert frames to greyscale, play in window
# type 'q' to quit
# from: https://docs.opencvs.org/3.0-beta/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2
import os

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/cv-py3/")

cap=cv2.VideoCapture('test.mp4')

while (cap.isOpened()):
	ret, frame = cap.read()

	gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cvs.destroyAllWindows()
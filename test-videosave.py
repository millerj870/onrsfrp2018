# ACTION:
# open saved movie, convert frames to greyscale, play in window
# type 'q' to quit
# from: https://docs.opencvs.org/3.0-beta/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2
import os

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/cv-py3/")

# Define the codec and create VideoWriter object
fourcc=cv2.VideoWriter_fourcc("m","p","4","v")

cap=cv2.VideoCapture('test.mp4')
# size=(int(cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)))
## out=cv2.VideoWriter('testoutput.mp4',fourcc,20.0,(640,480))

# from StackOverflow article 18835941

if cap.isOpened():
	# get cap properties
	width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # float
	height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
	fps = cap.get(cv2.CAP_PROP_FPS)

out=cv2.VideoWriter('testoutput.mp4',fourcc,20.0,width,height)

while (cap.isOpened()):
	ret, frame = cap.read()

	gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(gray)

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cvs.destroyAllWindows()
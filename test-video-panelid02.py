# ACTION:
# open saved movie, use histogram backprojection to identify solar panel in each frame
# type 'q' to quit
# from: https://docs.opencvs.org/3.0-beta/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2
import os
import time

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/basics - video/")
timestr=time.strftime("%Y%m%d-%H%M%S")

cap=cv2.VideoCapture('test.mp4')
# get cap properties
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
size=(int(width),int(height))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc=cv2.VideoWriter_fourcc("m","p","4","v")
# fourcc=cv2.VideoWriter_fourcc("x","2","6","4")

out = cv2.VideoWriter(timestr+'-vidtest.mp4', fourcc,fps,size,True)


# load image that represents the patern/texture we are sarching for; conver
# to HSV image
roi=cv2.imread("panelcrop-sm-DC_0181.jpeg")
hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
# calculating histogram of ROI image
roihist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
# normalize the histogram 
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
# circular disk for convolution, below
disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))


while (cap.isOpened()):
	ret, frame = cap.read()

	if ret:
		# convert frame to HSV image
		hsvt=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	# apply backprojection with normalized ROI histogram
	dst=cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

	# convolute with circular disk
	cv2.filter2D(dst,-1,disk,dst)

	#threshold and binary AND
	ret2,thresh = cv2.threshold(dst,50,255,0)
	thresh=cv2.merge((thresh,thresh,thresh))
	res=cv2.bitwise_and(frame,thresh)

	if ret == True:
   		out.write(res)
		cv2.imshow('result',res)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
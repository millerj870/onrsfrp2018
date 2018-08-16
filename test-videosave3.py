# ACTION:
# open saved movie, convert frames to greyscale, play in window
# type 'q' to quit
# from: https://docs.opencvs.org/3.0-beta/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2
import os
import time

timestr=time.strftime("%Y%m%d-%H%M%S")

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/cv-py3/")

# Define the codec and create VideoWriter object

cap=cv2.VideoCapture('test.mp4')
# size=(int(cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)))
## out=cv2.VideoWriter('testoutput.mp4',fourcc,20.0,(640,480))

# get cap properties
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
size=(int(width),int(height))
fps = cap.get(cv2.CAP_PROP_FPS)
#fourcc=cv2.VideoWriter_fourcc("m","p","4","v")
fourcc=cv2.VideoWriter_fourcc("x","2","6","4")

### self.vout = cv2.VideoWriter()
### success = self.vout.open(timestr+'-vidtest.mp4', fourcc,fps,size,True)

out = cv2.VideoWriter(timestr+'-vidtest.mp4', fourcc,fps,size,True)

#out=cv2.VideoWriter(timestr+'-vidtest.mp4',fourcc,fps,size,True)

# fourcc=cv2.VideoWriter_fourcc("a","v","c","1")
# out=cv2.VideoWriter('textout.avi',fourcc,fps,size,True)
## fourcc=cv2.cv2.FOURCC("a","v","c","1")

while(cap.isOpened()):
   ret, frame = cap.read()
   gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   edges = cv2.Canny(gray,180,200,10)

   if ret == True:
   		out.write(edges)
   		cv2.imshow('edges',edges)

   if cv2.waitKey(1) & 0xFF == ord('q'):
   	    break;
 #  else:
 #		print 'Error...'
 #		break;

cap.release()
out.release()
cv2.destroyAllWindows()

# print width
# print height
# print fps
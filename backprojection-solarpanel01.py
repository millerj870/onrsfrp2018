import cv2
import numpy as np
import os
import time

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/basics - images/")
timestr=time.strftime("%Y%m%d-%H%M%S")

# load image that represents the patern/texture we are sarching for; conver
# to HSV image
roi=cv2.imread("panelcrop-sm-DC_0181.jpeg")
hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

# load image that contains the region we are looking for; conver
# to HSV image
target=cv2.imread("DC_0181.jpg")
hsvt=cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# calculating histogram of rio image
roihist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

# normalize the histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst=cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# convolute with circular disk
disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disk,dst)

#threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh=cv2.merge((thresh,thresh,thresh))
res=cv2.bitwise_and(target,thresh)

#res=np.vstack((target,thresh,res))
cv2.imwrite(timestr+'res.jpg',res)
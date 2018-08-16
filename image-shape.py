import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import time

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/basics - images/")
timestr=time.strftime("%Y%m%d-%H%M%S")

img = cv2.imread('DC_0181.jpg',1)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


# OpenCV uses the BGR color format for images; matplotlib uses RGB; 
# so one must manually change the format to use the latter after loading
# with the former (SO 15072736)

ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# cv2.imshow('image',thresh)
# cv2.waitKey(0)
# cvs.destroyAllWindows()

f, axarr = plt.subplots(1,2)
axarr[0].imshow(gray,cmap="gray")
axarr[1].imshow(thresh,cmap="gray")

plt.show()
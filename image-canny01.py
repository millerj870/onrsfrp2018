import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import time

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/basics - images/")
timestr=time.strftime("%Y%m%d-%H%M%S")

img = cv2.imread('DC_0181.jpg',1)

# OpenCV uses the BGR color format for images; matplotlib uses RGB; 
# so one must manually change the format to use the latter after loading
# with the former (SO 15072736)
b,g,r = cv2.split(img)
img2=cv2.merge([r,g,b])

# alternatively
# cvs.cvtColor(img,cvs.COLOR_BGR2RGB)
# or 
# img2 = img[...,::-1] 
# or
# img2 = img[:,:,::-1]

canny = cv2.Canny(img,180,200,10)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cvs.destroyAllWindows()


# plt.subplot(121);plt.imshow(img)
# plt.subplot(122);plt.imshow(img2)


f, axarr = plt.subplots(1,2)
axarr[0].imshow(img2)
axarr[1].imshow(canny)

plt.show()
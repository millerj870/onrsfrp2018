# from stackoverflow #10605163
# 180719 this appears to work

import numpy as np
import cv2
import os
import time

os.chdir("/Volumes/MoreRoom/Dropbox (CSUCI)/PROJECTS/_project - ONR Summer Faculty Research Program/subproject - learn OpenCV/cv-py3/")
timestr=time.strftime("%Y%m%d-%H%M%S")

def main():
	vc = cv2.VideoCapture()
	if not vc.open('test.mp4'):
		print('failed to open video capture')
		return

	fourcc=cv2.VideoWriter_fourcc(*'mp4v')
	# Match sourve video features
	fps = vc.get(cv2.CAP_PROP_FPS)
	size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)),)

	vw = cv2.VideoWriter()
	if not vw.open(timestr+'-vidtest.mp4',fourcc,fps,size):
		print('failed to open video writer')
		return

	while True:
		ok, frame = vc.read()
		if not ok:
			break

		gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(gray,180,200,10)

		#Write processed frame
		vw.write(edges)

		cv2.imshow('frame with edges',edges)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	vc.release()
	vw.release()
	cv2.destroyAllWindows()



if __name__=="__main__":
	main()
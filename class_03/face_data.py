# Collect face data

#facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
#	faces = facec.detectMultiScale(gray, 1.3, 5)
#for (x,y,w,h) in faces:
#	fc = fr[y:y+h, x:x+w, :]
#cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)

import numpy as np
import cv2

cam = cv2.VideoCapture(0)
# cam1 = cv2.VideoCapture(1)

while True:
	ret, fr = cam.read()
	if ret == True:
		
		cv2.imshow('frame', fr)

		if cv2.waitKey(1) == 27:
		# if cv2.waitkey(1) & 0xFF == ord('q'):
			break
	else:
		print "error"
		break
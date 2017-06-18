# Collect face data

import numpy as np
import cv2

cam = cv2.VideoCapture(0)
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

data = []

while True:
	ret, fr = cam.read()
	if ret == True:
		gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
		faces = facec.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:
			fc = fr[y:y+h, x:x+w, :]
			r = cv2.resize(fc, (50, 50))

			cv2.rectangle(fr, (x, y), (x+w, y+h), (0, 0, 255), 2)
		
		cv2.imshow('fr', fr)
		if cv2.waitKey(1) == 27:
			break
	else:
		print "error"
		break
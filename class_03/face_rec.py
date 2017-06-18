# Face recognition
import numpy as np
import cv2

cam = cv2.VideoCapture(0)
facec = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

# Load data in train (X and y)

f_01 = np.load('face_01.npy').reshape((20, -1))
f_02 = np.load('face_02.npy').reshape((20, -1))
f_03 = np.load('face_03.npy').reshape((20, -1))

data = np.concatenate((f_01, f_02, f_03))
labels =  np.zeros((data.shape[0],))

labels[20:40] = 1.0
labels[40:] = 2.0

names = {
	0: 'Shubham',
	1: 'Laksh',
	2: 'Sachin'
}

# Define KNN functions

def distance(x1, x2):
	d = np.sqrt(((x1-x2)**2).sum())
	return d

def knn(X_train, y_train, xt, k=5):
	vals = []
	for ix in range(X_train.shape[0]):
		d = distance(X_train[ix], xt)
		vals.append([d, y_train[ix]])
	sorted_labels = sorted(vals, key=lambda z: z[0])
	neighbours = np.asarray(sorted_labels)[:k, -1]
	
	freq = np.unique(neighbours, return_counts=True)
	
	return freq[0][freq[1].argmax()]

# Run the main loop

while True:
	ret, fr = cam.read()
	if ret == True:
		gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
		faces = facec.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			# Extract detected face
			fc = fr[y:y+h, x:x+w, :]
			# resize to a fixed shape
			r = cv2.resize(fr, (50, 50)).flatten()

			text = names[int(knn(data, labels, r))]
			cv2.putText(fr, text, (x, y), font, 1, (255, 255, 0), 2)

			cv2.rectangle(fr, (x, y), (x+w, y+h), (0, 0, 255), 2)
		cv2.imshow('fr', fr)
		if cv2.waitKey(1) == 27:
			break
	else:
		print "error"
		break

cv2.destroyAllWindows()
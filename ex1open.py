import numpy as np
import imutils
import cv2
import math
font = cv2.FONT_HERSHEY_SIMPLEX
distance = 0.0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while (True):
	ret, frame = cap.read()
	#frame = cv2.resize(frame_1, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
	#cv2.imshow('frame',frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)	
	
	for (x,y,w,h) in faces:
		distancei = (2*3.14 * 180)/(w+h*360)*1000 + 3
		#print distancei
		distance = math.floor(distancei/2)
        	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,153,51),2)
        	roi_gray = gray[y:y+h, x:x+w]
        	roi_color = frame[y:y+h, x:x+w]
		cv2.putText(frame,'Distance = ' + str(distance) + ' Inch', (5,100),font,1,(255,255,255),2)
    		cv2.imshow('face detection', frame)
    		if cv2.waitKey(1) == ord('q'):
			break
	     
cap.release()
cv2.destroyAllWindow()

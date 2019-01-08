import numpy as np
import cv2
import time
import os
import random as rd

imgSave=[]
timeSave=[]
timeSub=0.2

cap = cv2.VideoCapture(0)

startTime=time.time()
while(cap.isOpened()):
	
	Time=time.time()-startTime
	ret, frame = cap.read()
	img= cv2.cvtColor(frame,0)

	timeSave=[Time]+timeSave
	imgSave=[img]+imgSave
	
	for i in range(len(timeSave)):
		if (Time-timeSave[i]>=timeSub):
			imgSub=imgSave[i]
			imgSave=imgSave[:i]
			timeSave=timeSave[:i]
			break

	try:
		imgsubstract=cv2.add(img,-imgSub)
		imgsubstract = cv2.threshold(imgsubstract,255*(0.8),255,cv2.THRESH_BINARY_INV)[1]
		img=cv2.add(img,imgsubstract)
		ret,thresh = cv2.threshold(imgsubstract,127,255,0)
		img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img,contours, -1, (0,0,0), 3)
		cv2.imshow('img',img)
		cv2.imshow('imgsubstract',imgsubstract)
		
	except:
		print("1")
		
	print("ok")
	
	
	
	
	
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
import numpy as np
import cv2
import time
import os
import sys

sensibilite=95/100
FPS=5

# imageFile=80000
imageFile=100
maxFile=2
imgSave=[]
timeSave=[]
timeWrite=time.time()-1/FPS
countImage=imageFile+1
countFile=maxFile+1

cap = cv2.VideoCapture(0)
chemin=os.path.dirname(os.path.realpath(__file__))+chr(92)#obtient le chemin du fichier .py

startTime=time.time()
while(cap.isOpened()):
	
	Time=time.time()-startTime
	ret, frame = cap.read()
	img= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	l,w=img.shape
	n=int((l+w)/2)

	img=cv2.blur(img,(int((1-sensibilite)*n),int((1-sensibilite)*n)))
	
	timeSave=[Time]+timeSave
	imgSave=[img]+imgSave
	
	for i in range(len(timeSave)):
		if (Time-timeSave[i]>=1/FPS):
			imgSub=imgSave[i]
			imgSave=imgSave[:i]
			timeSave=timeSave[:i]
			break
	if (time.time()-timeWrite>1/FPS):
		timeWrite=time.time()
		try:
			img=cv2.add(img,-imgSub)
			cv2.imshow('img',img)
		except:
			img=img
		img = cv2.threshold(img,255*(sensibilite),255,cv2.THRESH_BINARY_INV)[1]
		
		cv2.imshow('frame',img)
		ret,thresh = cv2.threshold(img,127,255,0)
		img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img,contours, -1, (0,0,0), 3)
		
		if (len(contours)>1):
			if(countImage>=imageFile):
				if (countFile>=maxFile):
					countFile=1
				else:
					countFile+=1
				recordTime=time.time()
				countImage=1
				timeFileWrite=time.time()
				fourcc = cv2.VideoWriter_fourcc(*'XVID')
				writing=chemin+str(countFile)+'.avi'
				out = cv2.VideoWriter(writing,fourcc, 20.0, (640,480))
			else:
				countImage+=1
			out.write(frame)
			
			pourcent=min(max(int(countImage/imageFile*10000)/100,0.01),99.99)
			spendTime=int((time.time()-recordTime)*100)/100
			
			leftTime=int( spendTime*(1/(pourcent/100)-1) *100)/100
			
			print("Fichier: "+writing)
			print("Processing: "+str(pourcent)+" %")
			print("spendTime: "+str(spendTime)+" sec")
			print("leftTime: "+str(leftTime)+" sec")
			print("countFile: "+str(countFile)+" / "+str(maxFile))
			print("countImage: "+str(countImage)+" / "+str(imageFile))
			print()
			
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
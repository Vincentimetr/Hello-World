import numpy as np
import cv2
import os

chemin=os.path.dirname(os.path.realpath(__file__))+chr(92)#obtient le chemin du fichier .py

cap = cv2.VideoCapture(chemin+'openVideo.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
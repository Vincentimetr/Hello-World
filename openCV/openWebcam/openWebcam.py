import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame,0)

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
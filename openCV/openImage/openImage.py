import numpy as np
import cv2
import os

chemin=os.path.dirname(os.path.realpath(__file__))+chr(92)#obtient le chemin du fichier .py

img=cv2.imread(chemin+'openImage.png',cv2.IMREAD_UNCHANGED)#ouvre l'image du chemin donné
cv2.imshow('OpenCV - Image',img)#montre l'image préalablement ouverte

cv2.waitKey(0)#attent qu'une touche soit rentrée
cv2.destroyAllWindows()#ferme toute les fenetres openCV
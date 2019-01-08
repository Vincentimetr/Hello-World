import time
import random as rd
import matplotlib.pyplot as plt


def step():
    global taille
    global MAP
    global newMAP
    global ratioCendre
    global ratioOff
    for i in range(1,len(MAP)-1):
        for j in range(1,len(MAP)-1):
            time.sleep(timeExec/(taille*taille))
            if (MAP[i][j]==0):#inbrulable
                if ():
                    newMAP[i][j]=1
                elif(False):
                    newMAP[i][j]=2
                elif(False):
                    newMAP[i][j]=3
                else:
                    newMAP[i][j]=0
            elif (MAP[i][j]==1):#brulable
                if  (rd.random()<ratioDebroussaillage):
                    newMAP[i][j]=0
                elif ((((MAP[i-1][j]==2)or(MAP[i][j-1]==2)or(MAP[i][j+1]==2)or(MAP[i+1][j]==2))and(rd.random()<ratioFeu))or(rd.random()<ratioApparition)):
                    newMAP[i][j]=2
                elif (False):
                    newMAP[i][j]=3
                else:
                    newMAP[i][j]=1
            elif (MAP[i][j]==2):#brule
                if   (False):
                    newMAP[i][j]=0
                elif(rd.random()<ratioOff):
                    newMAP[i][j]=1
                elif(rd.random()<ratioCendre):
                    newMAP[i][j]=3
                else:
                    newMAP[i][j]=2
            elif (MAP[i][j]==3):#brulé
                if  (rd.random()<ratioNetoyage):
                    newMAP[i][j]=0
                elif(False):
                    newMAP[i][j]=1
                elif(False):
                    newMAP[i][j]=2
                else:
                    newMAP[i][j]=3
    return
def save():
    global MAP
    global newMAP
    MAP,newMAP=newMAP,[[-1 for i in range(taille)] for i in range(taille)]
    return
def show():
    global MAP
    global timeExec
    global taille
    t1=time.time()
    for x in range(len(MAP)):
        for y in range(len(MAP)):
            if (MAP[x][y]==0):
                plt.scatter(x, y, s=None, c="white", marker='s', norm=None, vmin=0, vmax=1/taille, edgecolors=None)
            elif (MAP[x][y]==1):
                plt.scatter(x, y, s=None, c="green", marker='s', norm=None, vmin=0, vmax=1/taille, edgecolors=None)
            elif (MAP[x][y]==2):
                plt.scatter(x, y, s=None, c="red", marker='s', norm=None, vmin=0, vmax=1/taille, edgecolors=None)
            elif (MAP[x][y]==3):
                plt.scatter(x, y, s=None, c="black", marker='s', norm=None, vmin=0, vmax=1/taille, edgecolors=None)
            
    plt.draw()
    plt.pause(timeExec/10)
    plt.clf()
    return
def hint():
    
    return
def loop():
    global timeStep
    while True:
        timeStep=time.time()
        show()
        save()
        step()
        hint()

#parametres
taille=15
timeExec=0.001

ratioFeu=0.5

ratioOff=0.05
ratioCendre=0.2

ratioNetoyage=0.005

ratioPousse=0.005
ratioDebroussaillage=0.005
ratioApparition=0.00001

#Initialisations
newMAP=[[round(rd.random()*3) for i in range(taille)] for i in range(taille)]
MAP=[]
########
loop()
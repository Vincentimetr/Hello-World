import time
import random as rd
import matplotlib.pyplot as plt

def init(taille):
    return [[False for i in range(taille)] for i in range(taille)]

def init_random(taille,densite):
    MAP=[[False for i in range(taille)] for i in range(taille)]
    population=int(densite*taille*taille)
    n=0
    for i in range(population):
        x=int(rd.random()*(taille))
        y=int(rd.random()*(taille))
        MAP[x][y]=True
    return MAP

def init_gliderGun(MAP,taille,x,y,NORD,OUEST):
  
    X=[0 ,0 ]+[1 ,1 ]+[10,10,10]+[11,11]+[12,12]+[13,13]+[14]+[15,15]+[16,16,16]+[17]+[20,20,20]+[21,21,21]+[22,22]+[24,24,24,24]+[34,34]+[35,35]
    Y=[5 ,6 ]+[5 ,6 ]+[5 ,6 ,7 ]+[4 ,8 ]+[3 ,9 ]+[3 ,9 ]+[6 ]+[4 ,8 ]+[5 ,6 ,7 ]+[6 ]+[3 ,4 ,5 ]+[3 ,4 ,5 ]+[2 ,6 ]+[1 ,2 ,6 ,7 ]+[3 ,4 ]+[3 ,4 ]
    
    for i in range(len(X)):
        MAP[(x+X[i])][(5+Y[i])]=True

    return MAP



def step(MAP,tour,bordure):
    newMap=[[False for i in range(taille)] for i in range(taille)]
    tour+=1
    naissances=0
    morts=0
    for x in range(bordure,len(MAP)-bordure):
        for y in range(bordure,len(MAP)-bordure):
            nb_voisins=0
            try:
                if MAP[x-1][y-1]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x-1][y+0]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x-1][y+1]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x+0][y-1]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x+0][y+1]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x+1][y-1]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x+1][y+0]:
                    nb_voisins+=1
            except:
                pass
            try:
                if MAP[x+1][y+1]:
                    nb_voisins+=1
            except:
                pass
            if (nb_voisins==3 and not(MAP[x][y])):
                newMap[x][y]=True
                naissances+=1
            elif (not(nb_voisins==2 or nb_voisins==3) and (MAP[x][y])):
                newMap[x][y]=False
                morts+=1
            elif (MAP[x][y]):
                newMap[x][y]=True

    MAP=newMap
    return (tour,naissances,morts,MAP)
    
def affiche(MAP,saveMAP1):
    t1=time.time()
    for x in range(len(MAP)):
        for y in range(len(MAP)):
            if MAP[x][y]:
                plt.scatter(x, y, s=None, c="black", marker='s', norm=None, vmin=0, vmax=1/taille, edgecolors=None)
    plt.draw()
    plt.pause(minTime)
    plt.clf()
    return

def decrit(tour,population,densite,naissances,morts,MAP):
    string=""+"\n"
    string+="Tour: "+str(tour)+"\n"
    string+="Population: "+str(population)+"\n"
    string+="Densite: "+str(densite)+"\n"
    string+="Naissances: "+str(naissances)+"\n"
    string+="Morts: "+str(morts)+"\n"
    print(string)
    return
    
def loop(densite,minTime,taille,bordure):
    
    tour=0
    executionTime=0
    population=taille*taille*densite
    naissances=0
    morts=0

    # MAP=init_random(taille,densite)
    MAP=init(taille)
    MAP=init_gliderGun(MAP,taille,10,10,False,False)
    
    
    saveMAP1=[[False for i in range(taille)] for i in range(taille)]
    saveMAP2=[[False for i in range(taille)] for i in range(taille)]
    saveMAP3=[[False for i in range(taille)] for i in range(taille)]
    saveMAP4=[[False for i in range(taille)] for i in range(taille)]
    while(True):
        startTime=time.time()
        
        saveMAP4=saveMAP3
        saveMAP3=saveMAP2
        saveMAP2=saveMAP1
        saveMAP1=MAP
        (tour,naissances,morts,MAP)=step(MAP,tour,bordure)

        while(time.time()-startTime<minTime):
            pass

        population=population+naissances-morts
        densite=population/(taille*taille)
        # decrit(tour,population,densite,naissances,morts,MAP)
        affiche(MAP,saveMAP1)
        if (saveMAP2==MAP):
            break
        if (saveMAP3==MAP):
            break
        if (saveMAP4==MAP):
            break
    decrit(tour,population,densite,naissances,morts,MAP)
    return

taille=200 #Taille de la map
minTime=0.01 #Temps minimum d'exectution
bordure=1

loop(rd.random(),minTime,taille,bordure)
#Importation des modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Parametres
n=5
precision=100
SSID="gerysgq"
deltaH=0.1

#Variables globales
SEED=0
for i in SSID:
    SEED+=ord(i)
COUNT=0
MAP=[]

def randomProc():
    global COUNT
    COUNT+=1
    _str=str((SEED+COUNT)*((SEED+1)*(COUNT+1)))
    _str=str(_str).replace(".","")
    _return=int(_str[len(_str)//2]+_str[len(_str)//2+1])/precision
    return _return
def createMAP():
    global MAP
    x=[i/n for i in range(n) for j in range(n)]
    y=[j/n for i in range(n) for j in range(n)]
    z=[randomProc() for i in range(n*n)]
    MAP=[x,y,z]
    return

def getVoisins(i,j):
    voisins=[]
    if(i>0 and j<n-1):
        voisins.append((i-1)*n+(j+1))
    if(i>0        ):
        voisins.append((i-1)*n+(j+0))
    if(i>0 and j>0):
        voisins.append((i-1)*n+(j-1))
    if(i<n-1 and j<n-1):
        voisins.append((i+1)*n+(j+1))
    if(i<n-1        ):
        voisins.append((i+1)*n+(j+0))
    if(i<n-1 and j>0):
        voisins.append((i+1)*n+(j-1))
    if(j<n-1):
        voisins.append((i+0)*n+(j+1))
    if(        j>0):
        voisins.append((i+0)*n+(j-1))
    return voisins
def getSommets():
    sommets=[]
    z=MAP[2]
    for i in range(n):
        for j in range(n):
            voisins=getVoisins(i,j)
            indice=i*n+j
            hauteur=z[indice]
            count=0
            nbVoisins=len(voisins)
            for k in voisins:
                indiceVoisin=k
                hauteurVoisin=z[indiceVoisin]
                if hauteur<=hauteurVoisin:
                    count+=1
                    break
            if count==nbVoisins:
                sommets.append(indice)
    return sommets
def erosionMAP():
    z=MAP[2]
    penteMax=0
    indiceMax1=0
    indiceMax2=0
    for i in range(n):
        for j in range(n):
            indice=i*n+j
            hauteur=z[indice]
            voisins=getVoisins(i,j)
            for k in range(len(voisins)):
                indiceVoisin=voisins[k]
                hauteurVoisin=z[indiceVoisin]
                pente=abs(hauteur-hauteurVoisin)
                if pente>penteMax:
                    penteMax=pente
                    indiceMax1=indice
                    indiceMax2=indiceVoisin
    if z[indiceMax1]>z[indiceMax2]:
        z[indiceMax1]=max(0,min(1,z[indiceMax1]-deltaH*randomProc()))
        z[indiceMax2]=max(0,min(1,z[indiceMax2]+deltaH*randomProc()))
        print(1)
    else:
        z[indiceMax1]=max(0,min(1,z[indiceMax1]+deltaH*randomProc()))
        z[indiceMax2]=max(0,min(1,z[indiceMax2]-deltaH*randomProc()))
        print(2)
def ecoulementMAP():
    z=MAP[2]
    indiceMin=[0,0]
    hauteurMin=1
    for i in range(n):
        for j in range(n):
            indice=i*n+j
            hauteur=z[indice]
            if hauteur<hauteurMin:
                hauteurMin=hauteur
                indiceMin=[i,j]
    voisins=getVoisins(indiceMin[0],indiceMin[1])
    indiceMin=0
    hauteurMin=1
    for k in range(len(voisins)):
        indice=voisins[k]
        hauteur=z[indice]
        if hauteur<hauteurMin:
            hauteurMin=hauteur
            indiceMin=indice
    z[indiceMin]=max(0,min(1,z[indiceMin]-deltaH*randomProc()))
    return

def techtonikMap():
    p1=[int(randomProc()*n),int(randomProc()*n)]
    p2=[int(randomProc()*n),int(randomProc()*n)]
    
    dx=(p2[0]-p1[0])
    dy=(p2[1]-p1[1])
    
    if dx==0:
        a=99999
    else:
        a=dy/dx
    b=p1[1]-a*p1[0]

    for x in [i for i in range(n)]:
        y=int(a*x+b)
        if y<0:
            pass
        elif y>1:
            break
        else:
            indice=n*y+x
            MAP[2][indice]=max(0,min(1,MAP[2][indice]+deltaH*randomProc()))
    return

def afficheMAP():
    plt.cla()
    ax.plot_trisurf(np.array(MAP[0]),np.array(MAP[1]),np.array(MAP[2]))
    plt.pause(0.001)
    return
def moyenneMAP():
    moyenne=0
    for i in MAP[2]:
        moyenne+=i
    return moyenne/(n*n)

#Execution
createMAP()
fig=plt.figure()
ax=fig.gca(projection='3d')

while True:
    moyenne=moyenneMAP()
    print(moyenne)
    print(getSommets())
    if moyenne>0.5:
        erosionMAP()
        ecoulementMAP()
    else:
        techtonikMap()
    afficheMAP()
#Import
import numpy as np
import tkinter 
from random import *
from copy import *
from time import *


#Settings
trainIn=[[1,1],[1,0]]
trainOut=[[0,1],[4,3]]
neurons=[]
population=10
mutation=0.01
selection=0.5

#Functions
    #Create
def create_POIDS(neurons):
    POIDS=[]
    for i in range (len(neurons)-1):
        POIDS.append([])
        for j in range (neurons[i]):
            POIDS[i].append([])
            for k in range (neurons[i+1]):
                POIDS[i][j].append(random())
    return POIDS
def create_GENERATION(population,neurons):
    GENERATION=[]
    for i in range(population):
        GENERATION.append(create_POIDS(neurons))
    return GENERATION
    #Calcul
def calcul_sortie(IN,POIDS,neurons):
    NEURONS=[IN]
    for i in range(1,len(neurons)):
        NEURONS.append([])
        for j in range(neurons[i]):
            NEURONS[i].append(0)
    for i in range(len(POIDS)):
        for j in range(len(POIDS[i])):
            neuron=0
            for k in range(len(POIDS[i][j])):
                NEURONS[i+1][k]+=NEURONS[i][j]*POIDS[i][j][k]
    return NEURONS[-1]
def calcul_ecart(GENERATION,trainIn,trainOut):
    ECARTS=[]
    for i in range(len(GENERATION)):
        ecart=0
        for j in range(len(trainIn)):
            sortie=calcul_sortie(trainIn[j],GENERATION[i],neurons)
            for k in range(len(trainIn[j])):
                ecart+=abs(trainOut[j][k]-sortie[k])
        ECARTS.append(ecart)
    return ECARTS
    #Mute
def mute_POIDS(POIDS,mutation):
    POIDS_copy=deepcopy(POIDS)
    for i in range(len(POIDS_copy)):
        for j in range(len(POIDS_copy[i])):
            for k in range(len(POIDS_copy[i][j])):
                POIDS_copy[i][j][k]*=1+mutation*(2*random()-1)
    return POIDS_copy
def mute_GENERATION(GENERATION,mutation,selection):
    n=int(len(GENERATION)*selection)
    population=len(GENERATION)
    for i in range(n,population):
        GENERATION[i]=mute_POIDS(GENERATION[i%n],mutation)
    return GENERATION
    #Tri
def tri_GENERATION(GENERATION,ECARTS):#Tri par insertion de ECARTS qui tri GENERATION par respect de l'ordre
    for i in range(1,len(ECARTS)):
        x=ECARTS[i]
        y=GENERATION[i]
        j=i
        while j>0 and ECARTS[j-1]>x:
            ECARTS[j]=ECARTS[j-1]
            GENERATION[j]=GENERATION[j-1]
            j=j-1
        ECARTS[j]=x
        GENERATION[j]=y
    return GENERATION
#Init
seed(0)
neurons=[len(trainIn[0])]+neurons+[len(trainOut[0])]
GENERATION=create_GENERATION(population,neurons)

#Train
generation=0
t_0=time()
ECARTS=calcul_ecart(GENERATION,trainIn,trainOut)
GENERATION=tri_GENERATION(GENERATION,ECARTS)
while ECARTS[0]!=ECARTS[int(population*selection)]:
    #Compteurs
    generation+=1
    temps=time()-t_0
    #Affichage
    print()
    print("#"*50)
    print("generation: "+str(generation))
    print("temps: "+str(temps))
    print("ecart: "+str(ECARTS[0]))
    #Amelioration
    ECARTS=calcul_ecart(GENERATION,trainIn,trainOut)
    GENERATION=tri_GENERATION(GENERATION,ECARTS)
    GENERATION=mute_GENERATION(GENERATION,mutation,selection)
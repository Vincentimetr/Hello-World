from random import *
from time import *

def createPoids(NEURONS):
    poids=[]
    for i in range(len(NEURONS)-1):
        poids.append([])
        for j in range(NEURONS[i]*NEURONS[i+1]):
            poids[i].append(random())
    return poids
def createPOIDS(NEURONS,nbPoids):
    POIDS=[]
    for i in range(nbPoids):
        POIDS.append(createPoids(NEURONS))
    return POIDS
def createVALUES(NEURONS):
    VALUES=[]
    for i in range(len(NEURONS)):
        VALUES.append([])
        for j in range(NEURONS[i]):
            VALUES[i].append(0)
    return VALUES
def mutePoids(poids,ratioMutation):
    for i in range(len(poids)):
        liens=poids[i]
        for j in range(len(liens)):
            lien=liens[j]
            mutation=(1-2*random())*ratioMutation
            lienNew=lien+mutation
            liens[j]=lienNew
    return poids
def mutePOIDS():
    global POIDS
    for i in range(1,len(POIDS)):
        poids=POIDS[i]
        ratioMutation=i/len(POIDS)
        POIDS[i]=mutePoids(poids,ratioMutation)
    return POIDS
def testPoids(poids,INPUTS,NEURONS):
    global POIDS,VALUES
    VALUES=[INPUTS]+createVALUES(NEURONS)[1:]
    nbCouches=len(NEURONS)
    for i in range(1,nbCouches):
        nbNeurons=NEURONS[i]
        nbNeuronsPrecedant=NEURONS[i-1]
        for j in range(nbNeurons):        
            for k in range(nbNeuronsPrecedant):
                poid=poids[i-1][nbNeurons*k+j]
                addValue=VALUES[i-1][k]*poid
                VALUES[i][j]+=addValue
    outputs=VALUES[-1]
    return outputs
def scorePoids(poids,TRAIN,NEURONS):
    score=0
    for i in range(len(TRAIN)):
        INPUTS=TRAIN[i][0]
        outputsPoids=testPoids(poids,INPUTS,NEURONS)
        for j in range(NEURONS[-1]):
            outputsTrain=TRAIN[i][1]
            score+=abs(outputsTrain[j]-outputsPoids[j])
    return score
def sortScores(scores):
    global POIDS,VALUES
    for i in range(1,len(scores)):
        x=scores[i]
        y=POIDS[i]
        j=i
        while j>0 and scores[j-1]>x:
            scores[j]=scores[j-1]
            POIDS[j]=POIDS[j-1]
            j=j-1
        scores[j]=x
        POIDS[j]=y
    return POIDS
def sortPOIDS(TRAIN,ratioSelection,NEURONS):
    global POIDS,VALUES
    scores=[]
    for i in range(len(POIDS)):
        poids=POIDS[i]
        score=scorePoids(poids,TRAIN,NEURONS)
        scores.append(score)
    POIDS=sortScores(scores)
    print(scores)
    return POIDS
def train(TRAIN,timeTrain,ratioSelection,NEURONS,ratioMutation,nbPoids):
    global POIDS,VALUES
    timeStart=time()
    while time()-timeStart<timeTrain:
        POIDS=mutePOIDS()
        POIDS=sortPOIDS(TRAIN,ratioSelection,NEURONS)
        nbDelete=int(len(POIDS)*ratioSelection)
        POIDS=POIDS[:-nbDelete]
        for i in range(nbDelete):
            POIDS+=[createPoids(NEURONS)]
    return POIDS
def learn(NEURONS,TRAIN,nbPoids,timeTrain,ratioSelection,ratioMutation):
    global POIDS,VALUES
    POIDS=createPOIDS(NEURONS,nbPoids)
    VALUES=createVALUES(NEURONS)
    POIDS=train(TRAIN,timeTrain,ratioSelection,NEURONS,ratioMutation,nbPoids)
    return POIDS

NEURONS=[2,1]
TRAIN=[[[1,1],[2]],[[1,-1],[3]]]
nbPoids=100
timeTrain=5
ratioSelection=0.5
ratioMutation=0.5

POIDS=learn(NEURONS,TRAIN,nbPoids,timeTrain,ratioSelection,ratioMutation)
bestPoids=POIDS[0]
score=scorePoids(bestPoids,TRAIN,NEURONS)
returning=testPoids(bestPoids,TRAIN[0][0],NEURONS)

print("score: "+str(score))
print("bestPoids: "+str(bestPoids))
print("returning: "+str(returning))
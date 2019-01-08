# -*- coding: utf-8 -*-

Output=[17,7,21,20,14,11] #Dans l ordre de en haut a droite vers en bas a gauche
import copy

SOLUTION=[]
Input=[1,2,3,4,5,6,7,8,9]
for i1 in range(9):
    for i2 in range(9):
        if not(i2 in [i1]):
            for i3 in range(9):
                if not(i3 in [i1,i2]):
                    for i4 in range(9):
                        if not(i4 in [i1,i2,i3]):
                            for i5 in range(9):
                                if not(i5 in [i1,i2,i3,i4]):
                                    for i6 in range(9):
                                        if not(i6 in [i1,i2,i3,i4,i5]):
                                            for i7 in range(9):
                                                if not(i7 in [i1,i2,i3,i4,i5,i6]):
                                                    for i8 in range(9):
                                                        if not(i8 in [i1,i2,i3,i4,i5,i6,i7]):
                                                            for i9 in range(9):
                                                                if not(i9 in [i1,i2,i3,i4,i5,i6,i7,i8]):
                                                                
                                                                    L1=[Input[i1],Input[i2],Input[i3]]
                                                                    L2=[Input[i4],Input[i5],Input[i6]]
                                                                    L3=[Input[i7],Input[i8],Input[i9]]
                                                                    
                                                                    
                                                                    Ligne_1_resolu=L1[0]+L1[1]+L1[2]==Output[0]
                                                                    Ligne_2_resolu=L2[0]+L2[1]+L2[2]==Output[1]
                                                                    Ligne_3_resolu=L3[0]+L3[1]+L3[2]==Output[2]
                                                                    Colonne_3_resolu=L1[2]+L2[2]+L3[2]==Output[5]
                                                                    Colonne_2_resolu=L1[1]+L2[1]+L3[1]==Output[4]
                                                                    Colonne_1_resolu=L1[0]+L2[0]+L3[0]==Output[3]
                                                                    
                                                                    print(SOLUTION)
                                                                    print("\n"*5)
                                                                    print(str(L1[0])+"  | "+str(L1[1])+"  | "+str(L1[2])+"  || "+str(Output[0])+"   "+str(Ligne_1_resolu))
                                                                    print("_"*20)
                                                                    print(str(L2[0])+"  | "+str(L2[1])+"  | "+str(L2[2])+"  || "+str(Output[1])+"   "+str(Ligne_2_resolu))
                                                                    print("_"*20)
                                                                    print(str(L3[0])+"  | "+str(L3[1])+"  | "+str(L3[2])+"  || "+str(Output[2])+"   "+str(Ligne_3_resolu))
                                                                    print("_"*20)
                                                                    print("_"*20)
                                                                    print(str(Output[3])+" | "+str(Output[4])+" | "+str(Output[5]))
                                                                    print(str(Colonne_1_resolu)+" | "+str(Colonne_2_resolu)+" | "+str(Colonne_3_resolu))
                                                                    
                                                                    if (Ligne_1_resolu and Ligne_2_resolu and Ligne_3_resolu and Colonne_1_resolu and Colonne_2_resolu and Colonne_3_resolu):
                                                                        SOLUTION.append(copy.deepcopy(L1+L2+L3))

print("\n"*30)
print("SOLUTIONS")
for solu in SOLUTION:
    print()
    print(str(solu[0])+"  | "+str(solu[1])+"  | "+str(solu[2])+"  || "+str(Output[0]))
    print("_"*20)
    print(str(solu[3])+"  | "+str(solu[4])+"  | "+str(solu[5])+"  || "+str(Output[1]))
    print("_"*20)
    print(str(solu[6])+"  | "+str(solu[7])+"  | "+str(solu[8])+"  || "+str(Output[2]))
    print("_"*20)
    print("_"*20)
    print(str(Output[3])+" | "+str(Output[4])+" | "+str(Output[5]))
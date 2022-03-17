"""
Created on Thu Mar 17 08:57:39 2022

@author: David LACAN
"""

import numpy as np
import datetime
import json

flag = 0
res = {"Porte-avions": ["D1", "D2", "D3","D4","D5"], "Contre-torpilleur 1":["E4","F4","G4"]}

print("Voici le dictionnaire \n",res)
print("\n voici le parcours du dictionnaire : \n")

for bateau, position in res.items():
        print(bateau,position)
case = input("Quelle case svp ?")

for bateau, position in res.items():
        for ligne in position:
            if(ligne == case):
                flag = 1

if(flag==1):
    print("touché")
else:
    print("raté")
 
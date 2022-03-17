#### Exercice 1
import json
nomFichier="randonneesgps.json"

#### Q11

def ex1q1(fichier):
    with open(fichier,"r") as f:
        donnees=json.load(f)
    print("Le nombre de randonnées est ",len(donnees))
    
    
#### Q12
def ex1q2(fichier):
    ListeNoms=[]
    with open(fichier,"r") as f:
        donnees=json.load(f)
    for randos in donnees:
        for cle_r,valeurs_r in randos.items():
            if cle_r=="Nom":
                ListeNoms.append(valeurs_r)
    print(ListeNoms)
           
ex1q1(nomFichier)
ex1q2(nomFichier)
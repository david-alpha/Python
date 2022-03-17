import json
nomFichier="randonneesgps.json"

#### Q11

def ex1q1(fichier):
    with open(fichier,"r") as f:
        donnees=json.load(f)
    print("Le nombre de randonnées est ",len(donnees))
BaseEtudiants = """2021420025;BLANC;Ludovic
2021421143;DUPOND;Claire
2021420247;DURAND;Juliette
2021420009;MARTIN;Alexandre
2021422278;PERRIN;Laurent"""

def Ex2(ListeEtudiants):
    lignes=ListeEtudiants.split('\n')
    dicoEtudiants={}
    for ligne in lignes:
        donnees=ligne.split(';')
        dicoEtudiants[donnees[0]]=donnees[2]+' '+donnees[1]
    return dicoEtudiants
	

print(Ex2(BaseEtudiants))

import json
from graphh import GraphHopper


# ____ Définitions de fonctions________________________________________________
def lire_cle(fic, api_name):
    # _________________________________________________________________________
    fp = open(fic, "r", encoding="utf8")  # ouverture du fichier en lecture
    dico = json.load(fp)                  # chargement de son contenu complet
    # print(dico, type(dico))
    cle = dico.get(api_name, None)        # cle = dico[api_name] ou None si abs
    return cle


def DistanceVilles(vildeb, vilfin, cli):
    # __Q 2-4_______________________________________________________________
    # address_to_Latitudelong traduit une localisation en un tuple (Latitude, Longitude)
    LatitudeLongitude_vildeb = cli.address_to_latlong(vildeb)
    LatitudeLongitude_vilfin = cli.address_to_latlong(vilfin)
    # la méth distance calcule la distance par voiture entre 2 points fournis
    #  par coord gps sous la forme de deux tuples (Latitude, Longitude), unité km ou m
    dist = cli.distance([LatitudeLongitude_vildeb, LatitudeLongitude_vilfin], unit="km")
    return dist


def ListeAltitudes(lis_positions, cli):
    # __Q 2-5_______________________________________________________________
    lisalt = []
    for posit in lis_positions:
        # print(posit, type(posit))
        Latitude = posit.get("Latitude", None)
        Longitude = posit.get("Longitude", None)
        if Latitude and Longitude is not None:
            paire = (Latitude, Longitude)
            # la meth elevation_point convertit un tuple (Latitude, Longitude) en une alt
            alt = cli.elevation_point(paire)
            lisalt.append(alt)
    return lisalt
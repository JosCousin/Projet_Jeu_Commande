
from Personnage.classes import Classe


class ChoixClasse :
    def __init__(self):
        pass

    def choixClasse(self):
        
        print("Choisissez votre classe :")
        print("1. Guerrier")
        print("2. Mage")
        print("3. Voleur")
        choix = input("Entrez le numéro de la classe choisie : ")
        for classe in Classe:
            if classe.value[0] == int(choix):
                return classe.value[1]
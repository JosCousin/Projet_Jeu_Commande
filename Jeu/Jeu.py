from Personnage.ChoixNom import *
from Personnage.ChoixClasse import *
from Personnage.VoirStat import *
from Personnage.personnage import *
from Donjon.grille import *
from Deplacement.deplacement import *
from Deplacement.VerifTypeSalle import *

class Jeu:

    def start(self):

        print("Bienvenue dans le jeu de combat !")
        print("Créez votre personnage :")

        choixNom = ChoixNom()
        choixClasse = ChoixClasse()
        voirStats = VoirStat()

        nom = choixNom.choixNom()

        classe = choixClasse.choixClasse()

        personnage = Personnage(nom, classe)

        voirStats.voirStats(personnage)

        print("Chargement de la carte...")

        donjon = creationGrille()
        print("Liste des grilles : ")
        for salle in donjon.listeSalle:
            print(salle.coordX, salle.coordY, salle.typeSalle)
        print("Grilles chargées !")

        print("Vous êtes actuellement en position (0, 0).\nVous pouvez vous déplacer en tapant les commandes suivantes :\nN pour aller au Nord\nS pour aller au Sud\nE pour aller à l'Est\nO pour aller à l'Ouest\nA pour avancer d'une case dans la direction actuelle\nG pour tourner à gauche\nD pour tourner à droite\nQ pour quitter le jeu\n")

        print("Vous êtes actuellement dans la salle (0, 0).\nVous êtes en direction du Nord.\nQuelle action voulez-vous effectuer ?")

        deplacement = Deplacement(personnage, donjon)
        stop = True

        while stop == True:
            nouvelle_grille = deplacement.deplacement()
            
            if nouvelle_grille is not None:
                donjon = nouvelle_grille
                deplacement = Deplacement(personnage, donjon)
                print("Nouvelle grille générée !")
                for salle in donjon.listeSalle:
                    print(salle.coordX, salle.coordY, salle.typeSalle)
                print("Grilles chargées !")
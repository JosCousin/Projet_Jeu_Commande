from Personnage.ChoixNom import *
from Personnage.ChoixClasse import *
from Personnage.VoirStat import *
from Donjon.grille import *
from Donjon.deplacement import *
from Donjon.VerifTypeSalle import *
print("Bienvenue dans le jeu de combat !")
print("Créez votre personnage :")

choixNom = ChoixNom()
choixClasse = ChoixClasse()
voirStats = VoirStat()

# -------------------Choix du Nom------------------ #

nom = choixNom.choixNom()

# -------------------Choix de la Classe------------------ #

personnage = choixClasse.choixClasse(nom)

# -------------------Affichage des Stats------------------ #
voirStats.voirStats(personnage)

# -------------------Début de l'Aventure------------------ #

print("Chargement de la carte...")

donjon = creationGrille()
print("Liste des grilles : ")
for salle in donjon.listeSalle:
    print(salle.coordX, salle.coordY, salle.typeSalle)
print("Grilles chargées !")

print("Vous êtes actuellement en position (0, 0).")
print("Vous pouvez vous déplacer en tapant les commandes suivantes :")
print("N pour aller au Nord")
print("S pour aller au Sud")
print("E pour aller à l'Est")
print("O pour aller à l'Ouest")
print("A pour avancer d'une case dans la direction actuelle")
print("G pour tourner à gauche")
print("D pour tourner à droite")
print("Q pour quitter le jeu")

# -------------------Déplacement------------------ #

print("Vous êtes actuellement dans la salle (0, 0).")
print("Vous êtes en direction du Nord.")
print("Quelle action voulez-vous effectuer ?")

deplacement = Deplacement(personnage, donjon)

while True:
    nouvelle_grille = deplacement.deplacement()
    
    if nouvelle_grille is not None:
        donjon = nouvelle_grille
        deplacement = Deplacement(personnage, donjon)
        print("Nouvelle grille générée !")
        for salle in donjon.listeSalle:
            print(salle.coordX, salle.coordY, salle.typeSalle)
        print("Grilles chargées !")
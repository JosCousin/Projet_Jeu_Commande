from Personnage.personnage import choixClasse, voirStats
from Personnage.personnage import choixNom
from Donjon.grille import creationGrille
from Donjon.donjon import creationDonjon
from Donjon.deplacement import deplacement

print("Bienvenue dans le jeu de combat !")
print("Créez votre personnage :")

# -------------------Choix du Nom------------------ #

nom = choixNom()

# -------------------Choix de la Classe------------------ #

personnage = choixClasse(nom)

# -------------------Affichage des Stats------------------ #
voirStats(personnage)

# -------------------Début de l'Aventure------------------ #

print("Chargement de la carte...")

donjon = creationDonjon()
print("Donjon créé !")
print("Nombre de grilles : ", donjon.nbGrilles)
print("Liste des grilles : ")
for grille in donjon.grilles:
    print("Grille en position (", grille.grilleX, ", ", grille.grilleY, ")")
print("Grilles chargées !")
grille = donjon.grilles[0]
for salle in grille.listeSalle:
    print("Salle en position (", salle.coordX, ", ", salle.coordY, "), de type ", salle.typeSalle)



# listeSalles = creationGrille()
# print("Liste des salles créée !")
# for salle in listeSalles:
#     print("Salle en position (", salle.coordX, ", ", salle.coordY, "), de type ", salle.typeSalle)
# print("Carte chargée !")


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

deplacement(personnage, grille.listeSalle)





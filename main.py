from personnage.personnage import choixClasse, voirStats
from personnage.personnage import choixNom
from Donjon.salle import creationSalle

print("Bienvenue dans le jeu de combat !")
print("Créez votre personnage :")

# -------------------Choix du Nom------------------ #

nom = choixNom()

# -------------------Choix de la Classe------------------ #

personnage = choixClasse()

# -------------------Affichage des Stats------------------ #

print("Voulez-vous voir les stats de votre personnage ?")
choix = input("Oui/Non : ")
if choix == "Oui" or choix == "oui" or choix == "O" or choix == "o":
    voirStats(personnage(nom))
else:
    print("Très bien, bonne aventure !")

# -------------------Début de l'Aventure------------------ #

print("Chargement de la carte...")

listeSalles = creationSalle()

print("Carte chargée !")


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
action = input("Entrez une commande : ")
if action == "N" or action == "n":
    print("Vous êtes maintenant en direction du Nord.")
    personnage.coordY += 1
    print("Vous entrez dans une nouvelle Salle en position (", personnage.coordX, ", ", personnage.coordY, ").")

    # if any(salle.coordX == personnage.cordX and salle.coordY == personnage.cordY for salle in listeSalles):
elif action == "S" or action == "s":
    print("Vous êtes maintenant en direction du Sud.")
    personnage.coordY -= 1
elif action == "E" or action == "e":
    print("Vous êtes maintenant en direction de l'Est.")
    personnage.coordX += 1
elif action == "O" or action == "o":
    print("Vous êtes maintenant en direction de l'Ouest.")
    personnage.coordX -= 1
# elif action == "A" or action == "a":
#     print("Vous avancez d'une case dans la direction actuelle.")
# elif action == "G" or action == "g":
#     print("Vous tournez à gauche.")
# elif action == "D" or action == "d":
#     print("Vous tournez à droite.")

elif action == "Q" or action == "q":
    print("Vous avez quitté le jeu.")
else:
    print("Commande invalide. Veuillez réessayer.")




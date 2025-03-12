class ChoixClasse :
    def __init__(self):
        pass

    def choixClasse(self, nom):
        from Personnage.Guerrier import Guerrier
        from Personnage.Mage import Mage
        from Personnage.Voleur import Voleur
        print("Choisissez votre classe :")
        print("1. Guerrier")
        print("2. Mage")
        print("3. Voleur")
        choix = input("Entrez le numéro de la classe choisie : ")
        if choix == "1":
            return Guerrier(nom)
        elif choix == "2":
            return Mage(nom)
        elif choix == "3":
            return Voleur(nom)
        else:
            print("Classe invalide, recommencez.")
            self.choixClasse(nom)
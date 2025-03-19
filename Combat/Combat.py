from Donjon.Monstre import Monstre


monstre = Monstre()
def combat(personnage):
    print(f"Vous êtes attaqué par un {monstre.nom} !")
    print(f"Le {monstre.nom} a {monstre.PV} points de vie.")
    print("Vous pouvez attaquer le monstre en tapant 'A' ou fuir en tapant 'F' mais vous perdrez 15 PV.")
    if input().lower() == "a":
        print("Vous attaquez le monstre !")
        monstre.PV -= personnage.force
        print(f"Le {monstre.nom} a maintenant {monstre.PV} points de vie.")
        if monstre.PV <= 0:
            print("Vous avez vaincu le monstre !")
        else:
            print("Le monstre vous attaque !")
            personnage.PV -= monstre.force
            print(f"Vous avez maintenant {personnage.PV} points de vie.")
            if personnage.PV <= 0:
                print("Vous avez été vaincu par le monstre.")
                return
            combat(personnage)
    else:
        if personnage.PV <= 15:
            print("Vous n'avez pas assez de points de vie pour fuir le combat.")
            print("Vous êtes vaincu par le monstre.")
            return
        print("Vous avez fui le combat.")
        personnage.PV -= 15
        print(f"Vous avez maintenant {personnage.PV} points de vie.")
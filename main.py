from Prompt.ConsoleUI import ConsoleUI
from Personnage.ChoixNom import ChoixNom
from Personnage.ChoixClasse import ChoixClasse
from Personnage.VoirStat import VoirStat
from Jeu.Jeu import Jeu

ui = ConsoleUI()

choixNom = ChoixNom(ui)
choixClasse = ChoixClasse(ui)
voirStats = VoirStat(ui)

jeu = Jeu(choixNom, choixClasse, voirStats, ui)
jeu.start()
from enum import Enum
from Deplacement.SalleEvenement.OnSalleVide import OnSalleVide
from Deplacement.SalleEvenement.OnMonstre import OnMonstre
from Deplacement.SalleEvenement.OnTresor import OnTresor
from Deplacement.SalleEvenement.OnMur import OnMur
from Deplacement.SalleEvenement.OnPorte import OnPorte
from Donjon.TypeSalle import TypeSalle

class ActionTypeSalle(Enum):
    SALLE_VIDE = OnSalleVide
    SALLE_MONSTRE = OnMonstre
    SALLE_TRESOR = OnTresor
    SALLE_MUR = OnMur
    SALLE_PORTE = OnPorte
from enum import Enum
from Deplacement.Mouvement.NordMouvement import NordMouvement
from Deplacement.Mouvement.SudMouvement import SudMouvement
from Deplacement.Mouvement.EstMouvement import EstMouvement
from Deplacement.Mouvement.OuestMouvement import OuestMouvement

class Direction(Enum):
    N = NordMouvement()
    S = SudMouvement()
    E = EstMouvement()
    O = OuestMouvement()


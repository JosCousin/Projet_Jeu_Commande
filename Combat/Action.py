from enum import Enum
from Combat.Attaque import Attaque
from Combat.Fuite import Fuite

class Action(Enum):
    A = Attaque
    F = Fuite
from enum import Enum, auto

class Tiles(Enum):
    EMPTY = auto()

    class Conveyor(Enum):
        UP = auto()
        UP_LEFT = auto()
        UP_RIGHT = auto()
        DOWN_LEFT = auto()
        DOWN_RIGHT = auto()
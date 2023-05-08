from enum import Enum, auto

class Tiles(Enum):
    EMPTY = auto()

class Conveyor(Enum):
    UP = "img/conveyor/up.png"
    UP_LEFT = "img/conveyor/up_left.png"
    UP_RIGHT = "img/conveyor/up_right.png"
    DOWN_LEFT = "img/conveyor/down_left.png"
    DOWN_RIGHT = "img/conveyor/down_right.png"

tilemap = [[Tiles.EMPTY for i in range(0, 30)] for i in range(0, 17)]
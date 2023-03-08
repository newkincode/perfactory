import lib.item as item

class Mining:
    def __init__(self, musPos) -> None:
        self.tilemap: list[list[int]] = [[]]
        self.pos: list = [musPos[0]//32*32,musPos[1]//32*32]
        self.tilePos: list = [musPos[0]//32,musPos[1]//32]

    def updata(self, map):
        self.tilemap: list[list[int]] = map
    
    def detect(self):
        for i in range(2,7):
            if self.tilemap[self.tilePos[1]][self.tilePos[0]-1] == i:
                return i
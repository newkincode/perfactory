import pygame
import lib.tile as tiles
import lib.draw as draw
import math
import json
from typing import Tuple, Dict

# 단어장
# mouses = mus

pygame.init()

# 변수
hw: tuple = (960, 640) # 창크기변수
screen: pygame.Surface = pygame.display.set_mode(hw)
runing: bool = True
var: str = "alpha 0.2"
tilemap: list[list[int]] = tiles.tileMap
# 마우스
musPos: tuple = pygame.mouse.get_pos()
cusImg: pygame.Surface = pygame.image.load("asset/img/mouseCus.png")
# 색
SKYBLUE = (113, 199, 245)
# 타일 이미지
tileImg: pygame.Surface = pygame.image.load("asset/img/tile.png")
conveyorBelt: dict[str, tuple[pygame.Surface, int]] = {
    "downUp" : (pygame.image.load("asset/img/conveyor_belt.png"),2),
    "upLeft" : (pygame.image.load("asset/img/conveyor_belt_up_left.png"),3),
    "leftRight" : (pygame.image.load("asset/img/conveyor_belt_left_right.png"),4)
}
machine: dict[str, tuple[pygame.Surface, int]] = {
    "mining" : (pygame.image.load("asset/img/mining_machine.png"),5),
}
stuff: dict[str, tuple[pygame.Surface, int]] = {
    "tree" : (pygame.image.load("asset/img/tree.png"),6),
}

# 아이템
# itemList: dict[str, int] = [2,3,4]
selectItem: int =  6
def opneDef():
    global selectItem
    try:
        save = open("data/playerData.json","r")
        saveData: dict = json.load(save)
        # selectItem: int = saveData["selectItem"]
    except:pass

# 세팅
pygame.display.set_caption(f"SFG2 {var}! - by newkini") # 창 이름
pygame.mouse.set_visible(False)

while runing:
    # 함수
    opneDef()

    # 변수
    musPos = pygame.mouse.get_pos()
    musTile: list = [math.trunc(musPos[0]/32), math.trunc(musPos[1]/32)]
    musTilePos: list = [32*musTile[0], 32*musTile[1]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    try:
        if pygame.mouse.get_pressed()[0] == 1:
            tilemap[musTile[1]][musTile[0]] = selectItem
            print(musTile)
    except:pass
    screen.fill(SKYBLUE)  # 화면 채우기
    draw.tileDraw(
        screen=screen,
        tilemap=tilemap,
        tileImg=tileImg,
        conveyorBelt=conveyorBelt,
        machine=machine,
        stuff=stuff
    )
    conveyorBelt["downUp"][0].set_alpha(128)
    screen.blit(conveyorBelt["downUp"][0],musTilePos)
    conveyorBelt["downUp"][0].set_alpha(255)
    screen.blit(cusImg,musPos)

    pygame.display.update()  # 화면 업데이트

pygame.quit()
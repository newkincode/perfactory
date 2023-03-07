import pygame
import lib.tile as tiles
import math
import json

# 단어장
# mouses = mus

pygame.init()

# 변수
hw: tuple = (960, 640) # 창크기변수
screen: pygame.Surface = pygame.display.set_mode(hw)
runing: bool = True
var: str = "alpha 0.2"
tilemap: list = tiles.tileMap
# 마우스
musPos: tuple = pygame.mouse.get_pos()
cusImg: pygame.Surface = pygame.image.load("asset/img/mouseCus.png")
# 색
SKYBLUE = (113, 199, 245)
# 타일 이미지
tileImg: pygame.Surface = pygame.image.load("asset/img/tile.png")
conveyorBeltImgs: dict[str, pygame.Surface] = {
    "downUp" : pygame.image.load("asset/img/conveyor_belt.png"),
    "upLeft" : pygame.image.load("asset/img/conveyor_belt_up_left.png"),
    "leftRight" : pygame.image.load("asset/img/conveyor_belt_left_right.png")
}

# 아이템
itemNumList: list = [2,3,4]
# itemList: dict[str, int] = [2,3,4]
selectItem: int = 1

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
            tilemap[musTile[1]][musTile[0]] = itemNumList[selectItem]
            print(musTile)
    except:pass
    screen.fill(SKYBLUE)  # 화면 채우기
    tilePos = [0, 0]
    for line in tilemap:
        for tile in line:
            screen.blit(tileImg, tilePos)
            if tile == 2:
                screen.blit(conveyorBeltImgs["downUp"], tilePos)
            if tile == 3:
                screen.blit(conveyorBeltImgs["upLeft"], tilePos)
            if tile == 4:
                screen.blit(conveyorBeltImgs["leftRight"], tilePos)
            tilePos[0] += 32
        tilePos[1] += 32
        tilePos[0] = 0
    
    conveyorBeltImgs["downUp"].set_alpha(128)
    screen.blit(conveyorBeltImgs["downUp"],musTilePos)
    conveyorBeltImgs["downUp"].set_alpha(255)
    screen.blit(cusImg,musPos)

    pygame.display.update()  # 화면 업데이트

pygame.quit()
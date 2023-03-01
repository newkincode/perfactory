import pygame
import lib.tile as tiles
import math
import json

# mouses = mus

pygame.init()

# 변수
hw = (960, 640)
screen = pygame.display.set_mode(hw)
runing = True
var = "alpha 0.1"
tilemap = tiles.tileMap
# 마우스
musPos = pygame.mouse.get_pos()
cusImg = pygame.image.load("asset/img/mouseCus.png")
# 색
SKYBLUE = (113, 199, 245)
# 타일 이미지
tileImg = pygame.image.load("asset/img/tile.png")
conveyorBeltImg = pygame.image.load("asset/img/conveyor_belt.png")
conveyorBeltImgUL = pygame.image.load("asset/img/conveyor_belt_ul.png")
conveyorBeltImgLR = pygame.image.load("asset/img/conveyor_belt_lr.png")
# conveyorBeltImg1.set_alpha(128)

# 아이템
itemList = [2,3,4]
selectItem = 1
conveyorBeltPosList = []

def opneDef():
    global selectItem
    try:
        save = open("data/playerData.json","r")
        saveData = json.load(save)
        selectItem = saveData["selectItem"]
    except:pass

# 세팅
pygame.display.set_caption(f"SFG2 {var}! - by newkini") # 창 이름
#pygame.mouse.set_cursor((32, 32),(0, 0),cusImg,(0,0))#(32,32),(0,0),(0,0),
print(pygame.cursors.arrow)
while runing:
    opneDef()
    musPos = pygame.mouse.get_pos()
    musTile = [math.trunc(musPos[0]/32), math.trunc(musPos[1]/32)]
    musTilePos = [32*musTile[0], 32*musTile[1]]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    try:
        if pygame.mouse.get_pressed()[0] == 1:
            tilemap[musTile[1]][musTile[0]] = itemList[selectItem]
            print(musTile)
    except:pass
    print(musTilePos)
    screen.fill(SKYBLUE)  # 화면 채우기
    tilePos = [0, 0]
    for line in tilemap:
        for tile in line:
            if (tile == 1) or (tile in itemList):
                screen.blit(tileImg, tilePos)
            if tile == 2:
                screen.blit(conveyorBeltImg, tilePos)
            if tile == 3:
                screen.blit(conveyorBeltImgUL, tilePos)
            if tile == 4:
                screen.blit(conveyorBeltImgLR, tilePos)
            tilePos[0] += 32
        tilePos[1] += 32
        tilePos[0] = 0
    
    conveyorBeltImg.set_alpha(128)
    screen.blit(conveyorBeltImg,musTilePos)
    conveyorBeltImg.set_alpha(255)

    pygame.display.update()  # 화면 업데이트

pygame.quit()
import pygame
import lib.tile as tiles
import math

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

# 아이템
itemList = [2]
selectItem = 0
conveyorBeltPosList = []

# 세팅
pygame.display.set_caption(f"SFG2 {var}! - by newkini") # 창 이름
#pygame.mouse.set_cursor((32, 32),(0, 0),cusImg,(0,0))#(32,32),(0,0),(0,0),
print(pygame.cursors.arrow)

while runing:
    musPos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                musTile = [math.trunc(musPos[0]/32), math.trunc(musPos[1]/32)]
                musTilePos = [musTile[0]*32, musTile[1]*32]
                conveyorBeltPosList.append(musTilePos)
                tilemap[musTile[1]][musTile[0]] = 2
                print(musTilePos)

    screen.fill(SKYBLUE)  # 화면 채우기
    tilePos = [0, 0]
    for line in tilemap:
        for tile in line:
            if (tile == 1) or (tile in itemList):
                screen.blit(tileImg, tilePos)
            tilePos[0] += 32
        tilePos[1] += 32
        tilePos[0] = 0
    pygame.display.update()  # 화면 업데이트

    for i in conveyorBeltPosList:
        screen.blit(conveyorBeltImg, i)

pygame.quit()
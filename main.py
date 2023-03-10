import pygame
import lib.tile as tiles
import lib.draw as draw
import math
import json
from typing import Tuple, Dict
import time
from tkinter import messagebox

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
tile: dict[str, tuple[pygame.Surface, int]] = {
    "conveyorBeltDownUp" : (pygame.image.load("asset/img/conveyor_belt.png"),2),
    "conveyorBeltUpLeft" : (pygame.image.load("asset/img/conveyor_belt_up_left.png"),3),
    "conveyorBeltLeftRight" : (pygame.image.load("asset/img/conveyor_belt_left_right.png"),4),
    "miningMachine" : (pygame.image.load("asset/img/mining_machine.png"),5),
    "tree" : (pygame.image.load("asset/img/tree.png"),6),
}

# 아이템
selectItem: int = 0
def opneDef():
    global selectItem
    try:
        save = open("data/playerData.json","r")
        saveData = json.load(save)
        selectItem = saveData["selectItem"]
    except:pass

# 세팅
pygame.display.set_caption(f"SFG2 {var}! - by newkini") # 창 이름
pygame.mouse.set_visible(False)

try:
    while runing:
        # 함수
        opneDef()

        # 변수
        musPos = pygame.mouse.get_pos()
        musTile: list = [math.trunc(musPos[0]/32), math.trunc(musPos[1]/32)]
        musTilePos: list = [32*musTile[0], 32*musTile[1]]

        # 키입력
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 나가기
                runing = False

        try: # 타일 설치
            if pygame.mouse.get_pressed()[0] == 1:
                tilemap[musTile[0]][musTile[1]] = selectItem
        except:pass

        # 그리기
        screen.fill(SKYBLUE)  # 화면 채우기
        draw.tileDraw( # 타일맵 그리기
            screen=screen,
            tilemap=tilemap,
            tileImg=tileImg,
            tiles=tile
        )
        tile["conveyorBeltDownUp"][0].set_alpha(128) # 반투명 설정
        screen.blit(tile["conveyorBeltDownUp"][0],musTilePos) # 유령 아이콘 그리기
        tile["conveyorBeltDownUp"][0].set_alpha(255) # 불투명 설정
        screen.blit(cusImg,musPos) # 커서 그리기

        pygame.display.update()  # 화면 업데이트
except BaseException as err:
    errMusic = pygame.mixer.Sound("asset/music/newkini.wav")
    errMusic.play()
    pygame.mouse.set_visible(True)
    print(err)
    messagebox.showerror("error", f"{err}")
    errMusic.stop()
    pygame.quit

pygame.quit()
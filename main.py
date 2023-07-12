import pygame
import math
from lib import factory
pygame.init()

# init
screen: pygame.Surface = pygame.display.set_mode((32*30, 32*17))
var: tuple[str, int, int, int] = ("alpha", 0, 0, 1)
pygame.display.set_caption(f"sfg2 {var[0]} {var[1]}.{var[2]}.{var[3]} by newkini")
clock = pygame.time.Clock()
is_running = True

# pygame.math.Vector2(
#             math.trunc(self.pos.x/32),
#             math.trunc(self.pos.y/32)
#         )

# main loop
while is_running:
    clock.tick(60)

    # update var
    mouse_pos = pygame.mouse.get_pos()
    select_tile = factory.Conveyor.UP

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    # mouse events
    if pygame.mouse.get_pressed()[0] == 1:
        tPos = pygame.Vector2(math.trunc(mouse_pos[0]/32), math.trunc(mouse_pos[1]/32))
        factory.tilemap[int(tPos.y)][int(tPos.x)] = select_tile

    # draw
    screen.fill(pygame.Color(255,255,255))

    # tile
    tilepos = pygame.Vector2(0, 0)
    for line in factory.tilemap:
        for tile in line:
            if tile == factory.Tiles.EMPTY:
                pass
            else:
                screen.blit(pygame.image.load(tile.value), (tilepos.x*32,tilepos.y*32))
            tilepos.x += 1
        tilepos.y += 1
        tilepos.x = 0

    # update
    pygame.display.update()
    
pygame.quit()
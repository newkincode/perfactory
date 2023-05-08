import pygame
pygame.init()

# init
screen: pygame.Surface = pygame.display.set_mode((800, 600))
var: tuple[str, int, int, int] = ("alpha", 0, 0, 0)
pygame.display.set_caption(f"sfg2 {var[0]} {var[1]}.{var[2]}.{var[3]} by newkini")
clock = pygame.time.Clock()
is_running = True

# main loop
while is_running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # update
    pygame.display.update()
    clock.tick(60)
pygame.quit()
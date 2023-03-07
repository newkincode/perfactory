def tileDraw(screen, tilemap, tileImg, conveyorBelt, machine, stuff):
    tilePos = [0, 0]
    for line in tilemap:
        for tile in line:
            screen.blit(tileImg, tilePos)
            if tile == 2:
                screen.blit(conveyorBelt["downUp"][0], tilePos)
            elif tile == 3:
                screen.blit(conveyorBelt["upLeft"][0], tilePos)
            elif tile == 4:
                screen.blit(conveyorBelt["leftRight"][0], tilePos)
            elif tile == 5:
                screen.blit(machine["mining"][0], tilePos)
            elif tile == 6:
                screen.blit(stuff["tree"][0], tilePos)
                print("a")
            tilePos[0] += 32
        tilePos[1] += 32
        tilePos[0] = 0
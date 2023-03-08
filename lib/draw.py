def tileDraw(screen, tilemap, tileImg, tiles):
    tilePos = [0, 0]
    for line in tilemap:
        for tile in line:
            screen.blit(tileImg, tilePos)
            for i in tiles:
                if tile == tiles[i][1]:
                    screen.blit(tiles[i][0], tilePos)
            tilePos[1] += 32
        tilePos[0] += 32
        tilePos[1] = 0
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import math
import pygame

xSize = 800
ySize = 600
cubeSize = 600/6
squareSize = cubeSize/9

bigOffset_X = xSize/2
bigOffset_Y = ySize/2
bigCubeSize = xSize/3
bigSquareSize = bigCubeSize/9

endgame = False

Face1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
Face2 = [[10, 11, 12],
            [13, 14, 15],
            [16, 17, 18]]
Face3 = [[19, 20, 21],
            [22, 23, 24],
            [25, 26, 27]]
Face4 = [[28, 29, 30],
            [31, 32, 33],
            [34, 35, 36]]
Face5 = [[37, 38, 39],
            [40, 41, 42],
            [43, 44, 45]]
Face6 = [[46, 47, 48],
            [49, 50, 51],
            [52, 53, 54]]

FaceList = [Face1, Face2, Face3, Face4, Face5, Face6 ]

currentFace = 1

def renderFaces():
    color = (255, 255, 255)
    surface.fill(pygame.Color(0, 0, 0, 255))
    #USAR r = pygame.Rect(tilesize_x * i, tilesize_y * j + screenOffset, tilesize_x, tilesize_y)
    #r.scale_by_ip(0.8)
    for i in FaceList:
        for j in i:
            for u in j:
                if FaceList.index(i) == currentFace - 1:
                    r = pygame.Rect(bigOffset_X + bigSquareSize * j.index(u), bigOffset_Y +
                                    (bigSquareSize * i.index(j)),
                                    bigSquareSize, bigSquareSize)
                    print(r)
                else:
                    r = pygame.Rect(squareSize * j.index(u), squareSize * i.index(j) +
                                    cubeSize*FaceList.index(i), squareSize, squareSize)
                #REVISA DE QUE COLOR ES EL CUADRADO U
                if(u < 55):
                    color = (255, 0, 0)
                if (u < 46):
                    color = (255, 255, 255)
                if (u < 37):
                    color = (0, 255, 0)
                if (u < 28):
                    color = (0, 0, 255)
                if (u < 19):
                    color = (255, 255, 0)
                if (u < 10):
                    color = (255, 106, 0)
                pygame.draw.rect(surface, color, r)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    pygame.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    surface = pygame.display.set_mode(size=(xSize, ySize), vsync=1)
    while not endgame:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if currentFace < 6:
                        currentFace += 1
                    else:
                        currentFace = 1
                    print("Cambiando a cara " + str(currentFace))
                    renderFaces()
                if event.key == pygame.K_UP:
                    print("Línea seleccionada: ")

    pygame.quit()


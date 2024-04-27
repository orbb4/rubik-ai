import random
import time
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
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

FaceList = [Face1, Face2, Face3, Face4, Face5, Face6]

currentFace = 1
currentLine = 2
currentColumn = 2
currentType = 0





def rotate(matrix):   #PA ROTAR LA MATRIZ 5 Y 6
    temp_matrix = []
    column = len(matrix) - 1
    for column in range(len(matrix)):
        temp = []
        for row in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[row][column])
        temp_matrix.append(temp)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
    return matrix

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

def rotateSelected():
    global Face1, Face2, Face3, Face4, Face5, Face6
    aux1 = copy.deepcopy(Face1)
    aux2 = copy.deepcopy(Face2)
    aux3 = copy.deepcopy(Face3)
    aux4 = copy.deepcopy(Face4)
    aux5 = copy.deepcopy(Face5)
    aux6 = copy.deepcopy(Face6)

    match currentType:
        case 0:                             #CASO LINEA
            match currentLine:
                case 1:                     #LINEA SUPERIOR
                    aux1[0] = Face4[0]
                    aux2[0] = Face1[0]
                    aux3[0] = Face2[0]
                    aux4[0] = Face3[0]

                    Face1[0] = aux1[0]
                    Face2[0] = aux2[0]
                    Face3[0] = aux3[0]
                    Face4[0] = aux4[0]

                    rotate(Face5)
                case 2:                     # LINEA SUPERIOR
                    aux1[1] = Face4[1]
                    aux2[1] = Face1[1]
                    aux3[1] = Face2[1]
                    aux4[1] = Face3[1]

                    Face1[1] = aux1[1]
                    Face2[1] = aux2[1]
                    Face3[1] = aux3[1]
                    Face4[1] = aux4[1]
                case 3:  # LINEA INFERIOR
                    aux1[2] = Face4[2]
                    aux2[2] = Face1[2]
                    aux3[2] = Face2[2]
                    aux4[2] = Face3[2]

                    Face1[2] = aux1[2]
                    Face2[2] = aux2[2]
                    Face3[2] = aux3[2]
                    Face4[2] = aux4[2]

                    rotate(Face6)
        case 1:             #CASO COLUMNA
            match currentFace:
                case 1:
                    match currentColumn:
                        case 1:
                            rotate(Face4)
                            for i in range(3):
                                aux1[i][0] = Face6[i][0]
                                aux5[i][0] = Face1[i][0]
                                aux3[i][2] = Face5[2-i][0]
                                aux6[i][0] = Face3[2-i][2]

                            for i in range(3):
                                Face6[i][0] = aux6[i][0]
                                Face1[i][0] = aux1[i][0]
                                Face5[i][0] = aux5[i][0]
                                Face3[i][2] = aux3[i][2]
                        case 2:
                            for i in range(3):
                                aux1[i][1] = Face6[i][1]
                                aux5[i][1] = Face1[i][1]
                                aux3[2-i][1] = Face5[i][1]
                                aux6[i][1] = Face3[2-i][1]

                            for i in range(3):
                                Face6[i][1] = aux6[i][1]
                                Face1[i][1] = aux1[i][1]
                                Face5[i][1] = aux5[i][1]
                                Face3[i][1] = aux3[i][1]
                        case 3:
                            rotate(Face2)
                            for i in range(3):
                                aux1[i][2] = Face6[i][2]
                                aux5[i][2] = Face1[i][2]
                                aux3[2-i][0] = Face5[i][2]
                                aux6[i][2] = Face3[2-i][0]

                            for i in range(3):
                                Face6[i][2] = aux6[i][2]
                                Face1[i][2] = aux1[i][2]
                                Face5[i][2] = aux5[i][2]
                                Face3[i][0] = aux3[i][0]
                case 2:
                    match currentColumn:
                        case 1:
                            rotate(Face1)
                            for i in range(3):
                                aux2[2-i][0] = Face6[0][i]
                                aux5[2][i] = Face2[i][0]
                                aux4[i][2] = Face5[2][2-i]
                                aux6[0][i] = Face4[i][2]

                            for i in range(3):
                                Face6[0][i] = aux6[0][i]
                                Face2[i][0] = aux2[i][0]
                                Face5[2][i] = aux5[2][i]
                                Face4[i][2] = aux4[i][2]
                        case 2:
                            for i in range(3):
                                aux2[2-i][1] = Face6[1][i]
                                aux5[1][i] = Face2[i][1]
                                aux4[i][1] = Face5[1][2-i]
                                aux6[1][i] = Face4[i][1]

                            for i in range(3):
                                Face6[1][i] = aux6[1][i]
                                Face2[i][1] = aux2[i][1]
                                Face5[1][i] = aux5[1][i]
                                Face4[i][1] = aux4[i][1]
                        case 3:
                            rotate(Face3)
                            for i in range(3):
                                aux2[i][2] = Face6[2][2-i]
                                aux5[0][i] = Face2[i][2]
                                aux4[2-i][0] = Face5[0][i]
                                aux6[2][i] = Face4[i][0]
                            for i in range(3):
                                Face6[2][i] = aux6[2][i]
                                Face2[i][2] = aux2[i][2]
                                Face5[0][i] = aux5[0][i]
                                Face4[i][0] = aux4[i][0]
    return 1

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    #PREPARACIÓN INICIAL
    pygame.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    surface = pygame.display.set_mode(size=(xSize, ySize), vsync=1)
    renderFaces()
    while not endgame:
        pygame.display.flip()


        for event in pygame.event.get():
            renderFaces()
            if event.type == pygame.QUIT:
                endgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if currentFace < 2:
                        currentFace += 1
                    else:
                        currentFace = 1

                    print("Cambiando a cara " + str(currentFace))
                    currentLine = 2
                    currentColumn = 2
                if event.key == pygame.K_UP:
                    if currentLine > 1:
                        currentLine -= 1
                    else:
                        currentLine = 3
                    currentType = 0
                    print("Línea seleccionada: " + str(currentLine))
                if event.key == pygame.K_DOWN:
                    if currentLine < 3:
                        currentLine += 1
                    else:
                        currentLine = 1
                    currentType = 0
                    print("Línea seleccionada: " + str(currentLine))
                if event.key == pygame.K_RIGHT:
                    if currentColumn < 3:
                        currentColumn += 1
                    else:
                        currentColumn = 1
                    currentType = 1
                    print("Columna seleccionada: " + str(currentColumn))
                if event.key == pygame.K_LEFT:
                    if currentColumn > 1:
                        currentColumn -= 1
                    else:
                        currentColumn = 3
                    currentType = 1
                    print("Columna seleccionada: " + str(currentColumn))

                if event.key == pygame.K_z:
                    rotateSelected()
                #shuffle
                if event.key == pygame.K_s:
                    for i in range(random.randint(5, 30)):
                        print(i)
                        if random.random() < 0.5:
                            currentColumn=random.randint(1, 3)
                            currentType=1
                        else:
                            currentRow=random.randint(1, 3)
                            currentType=0
                        currentFace = random.randint(1, 6)
                        rotateSelected()
    pygame.quit()

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
endgame = False
FaceList = []

Face1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
Face2 = [[[10, 11, 12],
            [13, 14, 15],
            [16, 17, 18]]]
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

currentFace = 1

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
                if event.key == pygame.K_KP_ENTER:
                    print("a")
                if event.key == pygame.K_UP:
                    print("Línea seleccionada: ")

    pygame.quit()


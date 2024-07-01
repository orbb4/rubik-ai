import numpy as np
import kociemba
import pycuber
from pycuber.solver import CFOPSolver


def to_kociemba_format(pycuber_cube):
    cube_str = str(pycuber_cube).replace(" ", "").replace("[", "").replace("]", "").replace("\n", "")
    cube_list = []
    for num in range(len(cube_str)):
        cube_list.append(cube_str[num])
    cube_kociemba = []

    # U stickers
    for num in range(9):
        cube_kociemba.append(cube_list[num])

    # R stickers
    aux = 15
    for num in range(3):
        for num in range(3):
            cube_kociemba.append(cube_list[aux])
            aux += 1
        aux += 9
    # F stickers
    aux = 12
    for num in range(3):
        for num in range(3):
            cube_kociemba.append(cube_list[aux])
            aux += 1
        aux += 9
    # D
    aux = 45
    for num in range(9):
        cube_kociemba.append(cube_list[aux])
        aux += 1
    # L stickers
    aux = 9
    for num in range(3):
        for num in range(3):
            cube_kociemba.append(cube_list[aux])
            aux += 1
        aux += 9
    # L stickers
    aux = 18
    for num in range(3):
        for num in range(3):
            cube_kociemba.append(cube_list[aux])
            aux += 1
        aux += 9
    str_cube_kociemba = "".join(str(sticker) for sticker in cube_kociemba)
    return str_cube_kociemba


cube = pycuber.Cube()
kociemba_format = to_kociemba_format(cube)

solver = CFOPSolver(cube)
solution = solver.solve()
print("Pasos para resolver el cubo:")
print(len(solution))

import numpy as np
import kociemba
import pycuber
import random






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
    replacements = {
        'y': "U",
        'o': "R",
        'g': "F",
        'w': "D",
        "r": "L",
        "b": "B"
    }
    for sticker in str_cube_kociemba:
        str_cube_kociemba = str_cube_kociemba.replace(sticker, replacements[sticker])
    return str_cube_kociemba


movements = ["L", "R", "F", "B", "U", "L'", "R'", "F'", "B'", "U'"]
with open('./data/26scramble.txt', 'a') as file:
    for i in range(40000):
        cube = pycuber.Cube()
        for n_rotate in range(27):
            cube(random.choice(movements))
            print(cube)
            koc_cube = to_kociemba_format(cube)
            if n_rotate == 1:
                steps = 1
            else:
                solution = kociemba.solve(koc_cube)
                steps = len(solution.split())
            if n_rotate < steps:
                steps = n_rotate
            result = koc_cube + "-" + str(steps) + "\n"
            file.write(result)
            print(result)
        print("rotate:" + str(i))

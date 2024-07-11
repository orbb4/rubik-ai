import tensorflow
import time
from colorama import Fore
import pycuber
import random
import keras
from data_gen import to_kociemba_format
from load_model import kociemba_to_onehot
import copy


def a_star_search(initial_cube, solved_cube, model, movements, moves_initial_cube, is_greedy):
    open_list = [] # lista que contiene arreglos [nodo, padre del nodo, distancia de la solucion (h), movimientos aplicados, g]

    open_list.append([str(initial_cube), [], model.predict(kociemba_to_onehot(to_kociemba_format(str(initial_cube)))), moves_initial_cube, 0])
    closed_list = []
    solved = False
    while not solved:
        min_distance = open_list[0][2]
        i_min_distance = 0
        for i in range(len(open_list)):
            distance = open_list[i][2]
            if distance < min_distance:
                i_min_distance = i
                min_distance = distance
        current = open_list.pop(i_min_distance)
        moves_from_current = current[3]
        closed_list.append(current)
        for move in movements:
            in_open_list = False
            in_closed_list = False
            cube_aux = apply_moves(pycuber.Cube(), moves_from_current)
            if move.endswith("2"):
                cube_aux(move[0])
                cube_aux(move[0])
            else:
                cube_aux(move)
            # si está en la lista cerrada, se ignora.
            for c in closed_list:
                if c[0] == str(cube_aux):
                    in_closed_list= True
                    break
            if in_closed_list:
                continue
            # si no está en la lista abierta, se añade a la misma
            for c in open_list:
                if c[0] == str(cube_aux):
                    in_open_list = True
                    break
            g = current[4] + 1
            h = model.predict(kociemba_to_onehot(to_kociemba_format(str(cube_aux))))[0][0]
            if is_greedy:
                f = h
            else:
                f = g + h
            print(h)
            if not in_open_list:
                print("current[1]: " + str(current[1]))
                open_list.append([str(cube_aux), current[1] + [move], f, moves_from_current + [move], g])
            else:
                for c in open_list:
                    if g < c[4]:
                        c[1] = current[1] + [move]
                        c[2] = f
                        c[3] = moves_from_current + [move]
                        c[4] = g
            # verificar si el cubo se resuelve con este paso
            if str(cube_aux) == str(solved_cube):
                print("solved!")
                print_color_cube(str(initial_cube))
                for step in current[1] + [move]:
                    time.sleep(1)
                    apply_moves(initial_cube, [step])
                    #print_color_cube(past_cubes[len(past_cubes) - 1])
                    print_color_cube(str(initial_cube))
                return current[1] + [move]



def is_solved(cube):
    solved_state = pycuber.Cube()
    return str(cube) == str(solved_state)



def color_cube(char):
    color_codes = {
        'w': Fore.WHITE,
        'r': Fore.RED,
        'g': Fore.GREEN,
        'b': Fore.BLUE,
        'y': Fore.YELLOW,
        'o': Fore.CYAN,
    }
    return color_codes.get(char)


def print_color_cube(cube_representation):
    colored_line = ""
    counter = 0
    for line in cube_representation:
        counter += 1
        for char in line:

            if char in "wrgbyo":
                colored_line += color_cube(char) + "■"
            if char == " " or char == "\n":
                colored_line+=char
            if char == "[" or char == "]":
                colored_line+= Fore.WHITE + char

    print(colored_line)


def apply_moves(rubik_cube, move_list):
    for m in move_list:
        if m.endswith("2"):
            rubik_cube(m[0])
            rubik_cube(m[0])
        else:
            rubik_cube(m)
    return rubik_cube

def test_a_star(num_of_tests, num_of_scrambles):
    average_steps = 0
    for t in range(num_of_tests):
        solved_cube = pycuber.Cube()
        cube = pycuber.Cube()
        moves = []
        print("test " + str(t))
        for i in range(num_of_scrambles):
            move = random.choice(movements)
            cube(move)
            moves.append(move)
            print_color_cube(str(cube))
            time.sleep(0.05)
        solution_path = a_star_search(cube, solved_cube, model, movements, moves, False)
        if solution_path:
            print("Solución:", solution_path)
            average_steps+=len(solution_path)

    average_steps/=num_of_tests
    print(average_steps)
    return average_steps


tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)
movements = ["L", "R", "F", "B", "U", "L'", "R'", "F'", "B'", "U'", "R2", "L2", "U2", "D2", "F2"]

model = keras.models.load_model('./solverB.h5')

start_time = time.time()
test_a_star(1, 12)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)


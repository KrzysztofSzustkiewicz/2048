import os
import random
import getch

from math import fabs
from termcolor import colored

color_key = {0: 'white',
             2: 'red',
             4: 'green',
             8: 'cyan',
             16: 'yellow',
             32: 'magenta',
             64: 'green',
             128: 'cyan',
             256: 'yellow',
             512: 'magenta',
             1024: 'green',
             2048: 'blue'
             }

def elements_movement(size, matrix, reversion=None):
    for index in range(0, size):
        if reversion is 'yes':
            matrix[index] = list(reversed(matrix[index]))
        matrix[index] = list(filter(lambda x: x > 0, matrix[index]))
        while len(matrix[index]) < size:
            matrix[index].append(0)
        if reversion is 'yes':
            matrix[index] = list(reversed(matrix[index]))

def puts_random_2(times):
    random_1 = random.randrange(0, 4)
    random_2 = random.randrange(0, 4)
    for option in range(times):

        if array[random_1][random_2] == 0:
            array[random_1][random_2] = 2
        else:
            puts_random_2(1)

def search_for_zero():
    for row in array:
        if 0 in row:
            return 'lose'

def search_win_con(win_con):
    for row in array:
        if win_con in row:
            return 'win'


def clear():
    os.system('clear')


def print_line(x, y, z, i):
    for j in range(x, y):
        print("\n" * z, " " * (4 - len(str(array[i][j]))), colored(array[i][j], color_key[array[i][j]]), end='')


def print_array():
    clear()
    for i in range(0, len(array)):
        print_line(0, 1, 1, i)
        print_line(1, 2, 0, i)
        print_line(2, 3, 0, i)
        print_line(3, 4, 0, i)


def matrix_index_dictionaries_creation(size):
    global right
    global left
    global up
    global down

    right = {'index_a': 0,
             'index_b': -(size - 1),
             'index_c': 0,
             'index_d': -(size - 2),
             'index_e': size,
             'index_f': size - 1,
             }

    left = {'index_a': 0,
            'index_b': 0,
            'index_c': 0,
            'index_d': 1,
            'index_e': size,
            'index_f': size - 1,
            }

    up = {'index_a': 0,
          'index_b': 0,
          'index_c': 1,
          'index_d': 0,
          'index_e': size - 1,
          'index_f': size,
          }

    down = {'index_a': -(size - 1),
            'index_b': 0,
            'index_c': -(size - 2),
            'index_d': 0,
            'index_e': size - 1,
            'index_f': size,
            }


def matrix_addition(matrix, direction):
    a = direction['index_a']
    b = direction['index_b']
    c = direction['index_c']
    d = direction['index_d']
    e = direction['index_e']
    f = direction['index_f']
    for row in range(0, e):
        for column in range(0, f):
            if matrix[int(fabs(row + a))][int(fabs(column + b))] != 0 and matrix[int(fabs(row + a))][
                int(fabs(column + b))] == matrix[int(fabs(row + c))][
                int(fabs(column + d))]:
                matrix[int(fabs(row + a))][int(fabs(column + b))] = 2 * matrix[int(fabs(row + a))][
                    int(fabs(column + b))]
                matrix[int(fabs(row + c))][int(fabs(column + d))] = 0


size = 4
array = [0] * size
for i in range(size):
    array[i] = [0] * size

puts_random_2(2)

matrix_index_dictionaries_creation(size)

print_array()

while search_win_con(2048) is not 'win' and search_for_zero() is 'lose':

    print("\n\n", " "*2, "Operate with W S A D", "\n Your goal is to score 2048!")
    user_input = getch.getch()

    if user_input == "a":
        matrix_addition(array, left)
        elements_movement(size,array)
        puts_random_2(1)

    elif user_input == "d":
        matrix_addition(array, right)
        elements_movement(size, array,'yes')
        puts_random_2(1)

    elif user_input == "\x1b[A":
        matrix_addition(array, up)
        list_1 = []
        j = 0
        for k in range(0, 4):
            for i in range(0, 4):
                list_1.append(array[i][k])
            list_1 = list(filter(lambda x: x > 0, list_1))
            while len(list_1) < 4:
                list_1.append(0)
            for i in range(0, 4):
                array[i][k] = list_1[j]
                j += 1
            j = 0
            list_1 = []
        puts_random_2(1)

    elif user_input == "s":
        matrix_addition(array, down)
        list_1 = []
        j = 3
        for k in range(0, 4):
            for i in range(0, 4):
                list_1.append(array[3 - i][k])
            list_1 = list(filter(lambda x: x > 0, list_1))
            while len(list_1) < 4:
                list_1.append(0)
            for i in range(0, 4):
                array[i][k] = list_1[j]
                j -= 1
            j = 3
            list_1 = []
        puts_random_2(1)
    print_array()

if search_win_con(2048) is 'win':
    clear()
    print_array()
    print("\n"*2, " "*5, "YOU WON THE GAME!")
else:
    clear()
    print_array()
    print("\n "*2, " "*6, "GAME OVER!", "\n", " "*5, "NO MORE MOVES!\n")
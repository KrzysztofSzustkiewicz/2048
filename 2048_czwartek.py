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
             32: 'red',
             64: 'green',
             128: 'cyan',
             256: 'yellow',
             512: 'red',
             1024: 'green',
             2048: 'blue'
             }


def elements_in_row_movement(size, matrix, reversion=None):
    for index in range(0, size):
        if reversion is 'reversed':
            matrix[index] = list(reversed(matrix[index]))
        matrix[index] = list(filter(lambda x: x > 0, matrix[index]))
        while len(matrix[index]) < size:
            matrix[index].append(0)
        if reversion is 'reversed':
            matrix[index] = list(reversed(matrix[index]))


def elements_in_column_movement(size, matrix, reversion=None):
    for column in range(0, size):
        work_list = []
        j = 0
        for row in range(0, size):
            work_list.append(matrix[row][column])
        if reversion is 'reversed':
            work_list = list(reversed(work_list))
        work_list = list(filter(lambda x: x > 0, work_list))
        while len(work_list) < size:
            work_list.append(0)
        if reversion is 'reversed':
            work_list = list(reversed(work_list))
        for row in range(0, size):
            matrix[row][column] = work_list[j]
            j += 1

#Function puts_random places '2' or '4' in random place of matrix.
#Argument 'times' determines how many random numbers are placed on each move.

def puts_random_2(times):
    random_1 = random.randrange(0, 4)
    random_2 = random.randrange(0, 4)
    random_num = random.randrange(2,5,2)
    for option in range(times):
         if array[random_1][random_2] == 0:
            array[random_1][random_2] = random_num
         else:
            puts_random_2(1)

#Function search_for_zero looks through array for '0'.

def search_for_zero():
    for row in array:
        if 0 in row:
            return 'lose'

#Function search_win_con searches through array for win_con argument which is element that is required to win.

def search_win_con(win_con):
    for row in array:
        if win_con in row:
            return 'win'


def clear():
    os.system('clear')

#Function colored takes 2 arguments.
#Colored element and color key that takes information from color_key dictionary.

def print_line(x, y, z, i):
    for j in range(x, y):
        print("\n" * z, " " * (4 - len(str(array[i][j]))), colored(array[i][j], color_key[array[i][j]]), end='')


def print_array():
    clear()
    print(' ' * 5, 'Your score is %d' % score_game)
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

score_game = 0

#Function is called in matrix_addition.

def score_of_game(score_1):
    global score_game
    score_game += score_1

#After each move matrix_addition checks if adjacent elements for the move direction have the same value.
#If so, adds them.

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
                score_of_game(matrix[int(fabs(row + a))][int(fabs(column + b))])
                matrix[int(fabs(row + c))][int(fabs(column + d))] = 0



size = 4
array = [0] * size
for i in range(size):
    array[i] = [0] * size

puts_random_2(2)

matrix_index_dictionaries_creation(size)

print_array()


while search_win_con(2048) is not 'win' and search_for_zero() is 'lose':

    print('\n\n', ' ' * 2, 'Operate with W S A D', '\n Your goal is to score 2048!')
    user_input = getch.getch()


    if user_input == 'a':
        elements_in_row_movement(size, array)
        matrix_addition(array, left)
        elements_in_row_movement(size, array)
        puts_random_2(1)
    elif user_input == 'd':
        elements_in_row_movement(size, array, 'reversed')
        matrix_addition(array, right)
        elements_in_row_movement(size, array, 'reversed')
        puts_random_2(1)

    elif user_input == 'w':
        elements_in_column_movement(size, array)
        matrix_addition(array, up)
        elements_in_column_movement(size, array)
        puts_random_2(1)

    elif user_input == 's':
        elements_in_column_movement(size, array, 'reversed')
        matrix_addition(array, down)
        elements_in_column_movement(size, array, 'reversed')
        puts_random_2(1)

    print_array()


if search_win_con(2048) is 'win':
    print_array()
    print('\n'*2, ' '*5, 'YOU WON THE GAME!')

else:
    print_array()
    print('\n ' * 2, ' ' * 6, 'GAME OVER!', '\n', ' ' * 5, 'NO MORE MOVES!\n')
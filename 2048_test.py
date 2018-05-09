import os
import getch
import random
from termcolor import colored
from math import fabs


color_key = {0 : 'blue',
             2 : 'red',
             4 : 'green',
             8 : 'cyan',
             16 : 'yellow',
             32 : 'grey',
             64 : 'white',
             128 : 'cyan',
             256 :'green',
             512 :'yellow',
             1024 :'red',
             2048 :'white'}

row = 0
column = 0

col_1 = ( column + 1 )
col_2 = ( 2 - column )
col_3 = ( 3 - column )
row_1 = ( row + 1)
row_2 = ( 2 - row )
row_3 = ( 3 - row )

left = {'first':column,
        'second':col_1,
        'third':row,
        'fourth':row}

right = {'first':col_3,
         'second':col_2,
         'third':row,
         'fourth':row}

up = {'first':column,
      'second':column,
      'third':row,
      'fourth':row_1}

down = {'first':column,
        'second':column,
        'third':row_3,
        'fourth':row_2}

b = 4
macierz = [0] * b
for i in range(b):
    macierz[i] = [0] * b


def columns_addition(matrix,size,course):
    for row in range(0, size):
        for column in range(0, size - 1):
                if matrix[course['third']][course['first']] == matrix[course['fourth']][course['second']] and matrix[course['third']][course['first']] != 0:
                    matrix[course['third']][course['first']] = 2 * matrix[course['third']][course['first']]
                    matrix[course['fourth']][course['second']] = 0


def movement(func):
    for i in range(0, 4):
        macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
        while len(macierz[i]) < 4:
            func


def movement_ver(a1,a2,a3):
    lista2 = []
    j = 0
    for k in range(0, 4):
        for i in range(0, 4):
            lista2.append(macierz[a2][k])
        lista2 = list(filter(lambda x: x > 0, lista2))
        while len(lista2) < 4:
            lista2.append(0)
        for i in range(0, 4):
            macierz[i][k] = lista2[j]
            j += a3
        j = a1
        lista2 = []


def print_array(x,y,z,i):
    for j in range(x, y):
        print("\n"*z ," " * (4 - len(str(macierz[i][j]))), colored(macierz[i][j], color_key[(macierz[i][j])]),end='')


def print_array1():
    for i in range(0, len(macierz)):
            print_array(0,1,1,i)
            print_array(1,2,0,i)
            print_array(2,3,0,i)
            print_array(3,4,0,i)


def random_elements():
    d = random.randrange(0, 4)
    e = random.randrange(0, 4)
    if macierz[d][e] == 0:
        macierz[d][e] = 2
    else:
        random_elements()


def clr():
    os.system('clear')

clr()


def f_1():
    macierz[i].append(0)

def f_2():
    macierz[i].insert(0,0)

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
          'index_e': size -1,
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
            if matrix[int(fabs(row + a))][int(fabs(column + b))] != 0:
                if matrix[int(fabs(row + a))][int(fabs(column + b))] == matrix[int(fabs(row + c))][int(fabs(column + d))]:
                    matrix[int(fabs(row + a))][int(fabs(column + b))] = 2 * matrix[int(fabs(row + a))][int(fabs(column + b))]
                    matrix[int(fabs(row + c))][int(fabs(column + d))] = 0



for i in range(2):
    random_elements()

matrix_index_dictionaries_creation(b)
print_array1()

while True:

    print("\n\n", " ", "Operate with W S A D")

    x=getch.getch()

    clr()

    if x=="a":
        matrix_addition(macierz, left)
        movement(f_1)
        random_elements()

    elif x == "d":
        matrix_addition(macierz, right)
        movement(f_2)
        random_elements()

    elif x=="w":
        matrix_addition(macierz, up)
        movement_ver(0, i, 1)
        random_elements()

    elif x == "s":
        matrix_addition(macierz, down)
        movement_ver(3, 3-i, (-1) )
        random_elements()

    print_array1()




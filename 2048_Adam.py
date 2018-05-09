import os
import random


color_key = {0: 'cyan',
             2: 'red',
             4: 'green',
             8: 'white',
             16: 'yellow',
             32: 'grey',
             64: 'white',
             128: 'cyan',
             256: 'green',
             512: 'yellow',
             1024: 'red',
             2048: 'white'}

row = 0
column = 0

col_1 = ( column + 1 )
col_2 = ( 2 - column )
col_3 = ( 3 - column )
row_1 = ( row + 1)
row_2 = ( 2 - row )
row_3 = ( 3 - row )

left = {'first': column,
        'second': col_1,
        'third': row,
        'fourth': row}

right = {'first': col_3,
         'second': col_2,
         'third': row,
         'fourth': row}

up = {'first': column,
      'second': column,
      'third': row,
      'fourth': row_1}

down = {'first':column,
        'second':column,
        'third':row_3,
        'fourth':row_2}

b = 4
array = [0] * b
for i in range(b):
    array[i] = [0] * b


def columns_addition(matrix,size,course):
    for row in range(0, size):
        for column in range(0, size - 1):
                if matrix[course['third']][course['first']] == matrix[course['fourth']][course['second']] and matrix[course['third']][course['first']] != 0:
                    matrix[course['third']][course['first']] = 2 * matrix[course['third']][course['first']]
                    matrix[course['fourth']][course['second']] = 0


def movement(func):
    for i in range(0, 4):
        array[i] = list(filter(lambda x: x > 0, array[i]))
        while len(array[i]) < 4:
            return func


def movement_ver(a1,a2,a3):
    lista2 = []
    j = 0
    for k in range(0, 4):
        for i in range(0, 4):
            lista2.append(array[a1][k])
        lista2 = list(filter(lambda x: x > 0, lista2))
        while len(lista2) < 4:
            lista2.append(0)
        for i in range(0, 4):
            array[i][k] = lista2[j]
            j += a2
        j = a3
        lista2 = []


def print_line(x,y,z,i):
    for j in range(x, y):
        print("\n"*z ," " * (4 - len(str(array[i][j]))), array[i][j] , end='')


def print_array():
    for i in range(0, len(array)):
            print_line(0,1,1,i)
            print_line(1,2,0,i)
            print_line(2,3,0,i)
            print_line(3,4,0,i)


def random_elements():
    d = random.randrange(0, 4)
    e = random.randrange(0, 4)
    if array[d][e] == 0:
        array[d][e] = 2
    else:
        random_elements()


def clr():
    os.system('clear')


def f_1():
    array[i].append(0)


def f_2():
    array[i].insert(0,0)


for i in range(2):
    random_elements()


clr()


print_array()


while array!=2048:

    print("\n\n", " ", "Operate with W S A D")

    x=input()

    clr()

    if x == "a" :
        columns_addition(array,b,left)
        movement(f_1)
        random_elements()

    elif x == "d" :
        columns_addition(array, b,right)
        movement(f_2)
        random_elements()

    elif x == "w" :
        columns_addition(array, b, up)
        movement_ver(i, 1, 0)
        random_elements()

    elif x == "s" :
        columns_addition(array, b, down)
        movement_ver(3-i, (-1), 3 )
        random_elements()

    print_array()
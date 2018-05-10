import os
import random

size = 4
array = [0] * size
for i in range(size):
    array[i] = [0] * size
for i in range(2):
    array[random.randrange(size)][random.randrange(size)]=2

row = 0
column = 0

col_1 = ( column + 1 )
col_2 = ( 2 - column )
col_3 = ( 3 - column )
row_1 = ( row + 1)
row_2 = ( 2 - row )
row_3 = ( 3 - row )

left = {1: column,
        2: col_1,
        3: row,
        4: row}

right = {1: col_3,
         2: col_2,
         3: row,
         4: row}

up = {1: column,
      2: column,
      3: row,
      4: row_1}

down = {1: column,
        2: column,
        3: row_3,
        4: row_2}

def print_line(x,y,z,i):
    for j in range(x, y):
        print("\n"*z ," " * (4 - len(str(array[i][j]))), array[i][j] , end='')

def columns_addition(matrix,size,course):


    for row in range(0, size):
        for column in range(0, size - 1):
                if matrix[course[3]][course[1]] == matrix[course[4]][course[2]] and matrix[course[3]][course[1]] != 0:
                    matrix[course[3]][course[1]] = 2 * matrix[course[3]][course[1]]
                    matrix[course[4]][course[2]] = 0

def print_array():
    for i in range(0, len(array)):
            print_line(0,1,1,i
            print_line(1,2,0,i)
            print_line(2,3,0,i)
            print_line(3,4,0,i)

def random_elements():
    random_1 = random.randrange(0, 4)
    random_2 = random.randrange(0, 4)
    if array[random_1][random_2] == 0:
        array[random_1][random_2] = 2
    else:
        random_elements()


def clr():
    os.system('clear')

print_array()

while True:
    print("\n\n", " ", "Operate with W S A D")
    x = input()
    clr()
    if x == "a":
        columns_addition(array, size, left)
        for i in range(0, 4):
            array[i] = list(filter(lambda x: x > 0, array[i]))
            while len(array[i]) < 4:
                array[i].append(0)
        random_elements()
    elif x == "w":
        columns_addition(array, size, up)
        lista2 = []
        j = 0
        for k in range(0, 4):
            for i in range(0, 4):
                lista2.append(array[i][k])
            lista2 = list(filter(lambda x: x > 0, lista2))
            while len(lista2) < 4:
                lista2.append(0)
            for i in range(0, 4):
                array[i][k] = lista2[j]
                j += 1
            j = 0
            lista2 = []
        random_elements()
    elif x == "s":
        columns_addition(array, size, down)
        lista2 = []
        j = 3
        for k in range(0, 4):
            for i in range(0, 4):
                lista2.append(array[3 - i][k])
            lista2 = list(filter(lambda x: x > 0, lista2))
            while len(lista2) < 4:
                lista2.append(0)
            for i in range(0, 4):
                array[i][k] = lista2[j]
                j -= 1
            j = 3
            lista2 = []
        random_elements()
    elif x == "d":
        columns_addition(array,size,right)
        for i in range(0, 4):
            array[i] = list(filter(lambda x: x > 0, array[i]))
            while len(array[i]) < 4:
                array[i].insert(0, 0)
        random_elements()


    print_array()

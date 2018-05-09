from math import fabs
import random,os,sys,getch
from termcolor import colored

random_element = random.randrange(2,4,2)

color_key = {0: 'cyan',
             2: 'red',
             4: 'green',
             8: 'white',
             16 : 'yellow',
             32: 'grey',
             64 : 'white',
             128 : 'cyan',
             256:'green',
             512:'yellow',
             1024:'red',
             2048:'white',
             4096:'grey',
             8192: 'cyan'
             }

#Function dsd puts '2' or '4' in random place of created array

def puts_random(element):
    random_x = random.randrange(0, 4)
    random_y = random.randrange(0, 4)
    if matrix[random_x][random_y] == 0:
        matrix[random_x][random_y] = element
    else:
        puts_random()

def clr():
    os.system('clear')

def comparison_and_addition(a, b, c, d):
    if matrix[fabs(row + a)][fabs(column + b)] != 0:
        if matrix[fabs(row + a)][fabs(column + b)] == matrix[fabs(row + c)][fabs(column + d)]:
            matrix[fabs(row + a)][fabs(column + b)] = 2 * matrix[fabs(row + a)][fabs(column + b)]
            matrix[fabs(row + c)][fabs(column + d)] = 0

def columns_addition_left(matrix, size, direction):
    for row in range(0, size):
        for column in range(0, size - 1):
            right = {'index_a': 0,
                     'index_b': -(size - 1),
                     'index_c': 0,
                     'index_d': -(size - 2)
                     }

            left = {'index_a': 0,
                    'index_b': 0,
                    'index_c': 0,
                    'index_d': 1
                    }

            up = {'index_a': 0,
                  'index_b': 0,
                  'index_c': 1,
                  'index_d': 0
                  }

            down = {'index_a': -(size - 1),
                    'index_b': 0,
                    'index_c': -(size - 2),
                    'index_d': 0
                    }

            index_a = direction['index_a']
            index_b = direction['index_b']
            index_c = direction['index_c']
            index_d = direction['index_d']
            comparison_and_addition(index_a, index_b, index_c, index_d)


# Creates an array
clr()

matrix_size = 4
matrix = [0] * matrix_size
for i in range(matrix_size):
    matrix[i] = [0] * matrix_size


#Puts '2' in random place of the array twice at the beggining of the game

for i in range(2):
    puts_random(2)

#Print created array and hints
def print_matrix():
    i = 0
    j = 0
    mat_len = len(str(matrix[i][j]))
    mat_ij = matrix[i][j]

    for i in range(0, len(matrix)):
        for j in range(0, 1):
            print("\n", " " * (4 - mat_len), colored(mat_ij, color_key[mat_ij]), end='')
        for j in range(1, 2):
            print(" " * (4 - mat_len), colored(mat_ij, color_key[mat_ij]), end='')
        for j in range(2, 3):
            print(" " * (4 - mat_len), colored(mat_ij, color_key[mat_ij]), end='')
        for j in range(3, 4):
            print(" " * (4 - mat_len), colored(mat_ij, color_key[mat_ij]), end='')
print_matrix()

while True:

#Takes input from user
    try:
        print("\n\n"," ", "Operate with W S A D")
        x=getch.getch()
        clr()
        if x=="a":
            columns_addition_left(matrix, matrix_size, 'left')
            for i in range(0, 4):
                matrix[i] = list(filter(lambda x: x > 0, matrix[i]))
                while len(matrix[i]) < 4:
                    matrix[i].append(0)
            puts_random(random_element)
        elif x=="w":
            columns_addition_left(matrix, matrix_size, 'up')
            list2 = []
            j = 0
            for k in range(0, 4):
                for i in range(0, 4):
                    list2.append(matrix[i][k])
                list2 = list(filter(lambda x: x > 0, lista2))
                while len(list2) < 4:
                    list2.append(0)
                for i in range(0, 4):
                    matrix[i][k] = list2[j]
                    j += 1
                j = 0
                list2 = []
            puts_random(random_element)
        elif x == "s":
            columns_addition_left(matrix, matrix_size, 'down')
            lista2 = []
            j = 3
            for k in range(0, 4):
                for i in range(0, 4):
                    lista2.append(matrix[3-i][k])
                lista2 = list(filter(lambda x: x > 0, lista2))
                while len(lista2) < 4:
                    lista2.append(0)
                for i in range(0, 4):
                    matrix[i][k] = lista2[j]
                    j -= 1
                j = 3
                lista2 = []
            puts_random(random_element)
        elif x == "d":
            columns_addition_left(matrix, matrix_size, 'right')
            for i in range(0, 4):
                matrix[i] = list(filter(lambda x: x > 0, matrix[i]))
                while len(matrix[i]) < 4:
                     matrix[i].insert(0,0)
            puts_random(random_element)

    except:
        print("\nGAME OVER\n")
        break


#Prints modified array with specific color for each character

print_matrix()

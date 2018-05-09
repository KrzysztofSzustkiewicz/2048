import random,os,sys,getch
from termcolor import colored
from math import fabs

#Creates a dictionary of element's color

color_key = {'0': 'blue', '2': 'red', '4': 'green', '8': 'cyan', '16' : 'yellow', '32': 'grey', '64' : 'white', '128' : 'cyan',
             '256':'green','512':'yellow','1024':'red','2048':'white'}





#Function dsd puts '2' in random place of created array

def dsd():
    d = random.randrange(0, 4)
    e = random.randrange(0, 4)
    if macierz[d][e] == 0:
        macierz[d][e] = 2
    else:
        dsd()
def clr():
    os.system('clear')

def matrix_index_dictionaries_creation(size):
    global right
    global left
    global up
    global down
    
    right = {'index_a': 0,
             'index_b': -(size - 1),
             'index_c': 0,
             'index_d': -(size - 2),
             }

    left = {'index_a': 0,
            'index_b': 0,
            'index_c': 0,
            'index_d': 1,
            }

    up = {'index_a': 0,
          'index_b': 0,
          'index_c': 1,
          'index_d': 0,
          }

    down = {'index_a': -(size - 1),
            'index_b': 0,
            'index_c': -(size - 2),
            'index_d': 0,
            }



def matrix_addition(matrix, size, direction):
    for row in range(0, size):
        for column in range(0, size - 1):
            a = direction['index_a']
            b = direction['index_b']
            c = direction['index_c']
            d = direction['index_d']
            if matrix[fabs(row + a)][fabs(column + b)] != 0:
                if matrix[fabs(row + a)][fabs(column + b)] == matrix[fabs(row + c)][fabs(column + d)]:
                    matrix[fabs(row + a)][fabs(column + b)] = 2 * matrix[fabs(row + a)][fabs(column + b)]
                    matrix[fabs(row + c)][fabs(column + d)] = 0

# Creates an array
clr()
b = 4
macierz = [0] * b
for i in range(b):
    macierz[i] = [0] * b

#Puts '2' in random place of the array twice at the beggining of the game

for i in range(2):
    dsd()

#Print created array and hints

for i in range(0, len(macierz)):
    for j in range(0, 1):
        print("\n", " " * (4 - len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]), end='')
    for j in range(1, 2):
        print(" " * (4 - len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]), end='')
    for j in range(2, 3):
        print(" " * (4 - len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]), end='')
    for j in range(3, 4):
        print(" " * (4 - len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]), end='')


matrix_index_dictionaries_creation(b)


while True:

#Takes input from user
    try:
        print("\n\n"," ", "Operate with W S A D")
        x=getch.getch()
        clr()
        if x=="a":
            matrix_addition(macierz, b, left)
            for i in range(0, 4):
                macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
                while len(macierz[i]) < 4:
                    macierz[i].append(0)
            dsd()
        elif x=="w":
            matrix_addition(macierz, b, up)
            lista2 = []
            j = 0
            for k in range(0, 4):
                for i in range(0, 4):
                    lista2.append(macierz[i][k])
                lista2 = list(filter(lambda x: x > 0, lista2))
                while len(lista2) < 4:
                    lista2.append(0)
                for i in range(0, 4):
                    macierz[i][k] = lista2[j]
                    j += 1
                j = 0
                lista2 = []
            dsd()
        elif x == "s":
            matrix_addition(macierz, b, down)
            lista2 = []
            j = 3
            for k in range(0, 4):
                for i in range(0, 4):
                    lista2.append(macierz[3-i][k])
                lista2 = list(filter(lambda x: x > 0, lista2))
                while len(lista2) < 4:
                    lista2.append(0)
                for i in range(0, 4):
                    macierz[i][k] = lista2[j]
                    j -= 1
                j = 3
                lista2 = []
            dsd()
        elif x == "d":
            matrix_addition(macierz, b, right)
            for i in range(0, 4):
                macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
                while len(macierz[i]) < 4:
                     macierz[i].insert(0,0)
            dsd()

    except:
        print("\nGAME OVER\n")
        break


#Prints modified array with specific color for each character

    for i in range(0, len(macierz)):
        for j in range(0, 1):
            print("\n", " "*(4-len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]), end='')
        for j in range(1, 2):
            print(" "*(4-len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]), end='')
        for j in range(2, 3):
            print(" "*(4-len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]),  end='')
        for j in range(3, 4):
            print(" "*(4-len(str(macierz[i][j]))), colored(macierz[i][j], color_key[str(macierz[i][j])]),  end='')

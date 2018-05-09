import random,os,sys
from math import fabs

#Creates a dictionary of element's color


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

for i in macierz:
    print(i)

matrix_index_dictionaries_creation(b)


while True:

#Takes input from user

        print("\n\n"," ", "Operate with W S A D")
        x=input()
        clr()
        if x=="a":
            matrix_addition(macierz, left)
            for i in range(0, 4):
                macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
                while len(macierz[i]) < 4:
                    macierz[i].append(0)
            dsd()
        elif x=="w":
            matrix_addition(macierz, up)
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
            matrix_addition(macierz, down)
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
            matrix_addition(macierz, right)
            for i in range(0, 4):
                macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
                while len(macierz[i]) < 4:
                     macierz[i].insert(0,0)
            dsd()
        for i in macierz:
            print(macierz)

for i in macierz:
    print(macierz)

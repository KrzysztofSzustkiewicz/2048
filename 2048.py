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
print_matrix()py

while True:

#Takes input from user
    try:
        print("\n\n"," ", "Operate with W S A D")
        x=getch.getch()
        clr()
        if x=="a":
            for i in range(0, 4):
                for k in range(0, 3):
                    if matrix[i][k] == matrix[i][k + 1] and matrix[i][k] != 0:
                        matrix[i][k] = 2 * matrix[i][k]
                        matrix[i][k + 1] = 0
            for i in range(0, 4):
                matrix[i] = list(filter(lambda x: x > 0, matrix[i]))
                while len(matrix[i]) < 4:
                    matrix[i].append(0)
            puts_random(random_element)
        elif x=="w":
            for k in range(0, 4):
                for i in range(0, 3):
                    if matrix[i][k] == matrix[i + 1][k] and matrix[i][k] != 0:
                        matrix[i][k] = 2 * matrix[i][k]
                        matrix[i + 1][k] = 0
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
            for k in range(0, 4):
                for i in range(0, 3):
                    if matrix[3 - i][k] == matrix[2 - i][k] and matrix[3 - i][k] != 0:
                        matrix[3 - i][k] = 2 * matrix[3 - i][k]
                        matrix[2 - i][k] = 0
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
            for i in range(0, 4):
                for k in range(0,3):
                    if matrix[i][3-k] == matrix[i][2-k] and matrix[i][3-k] != 0:
                        matrix[i][3-k] = 2 * matrix[i][3-k]
                        matrix[i][2-k] = 0
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

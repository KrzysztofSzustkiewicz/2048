import random,os,sys,getch
from termcolor import colored

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





while True:

#Takes input from user
    try:
        print("\n\n"," ", "Operate with W S A D")
        x=getch.getch()
        clr()
        if x=="a":
            for i in range(0, 4):
                for k in range(0, 3):
                    if macierz[i][k] == macierz[i][k + 1] and macierz[i][k] != 0:
                        macierz[i][k] = 2 * macierz[i][k]
                        macierz[i][k + 1] = 0
            for i in range(0, 4):
                macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
                while len(macierz[i]) < 4:
                    macierz[i].append(0)
            dsd()
        elif x=="w":
            for k in range(0, 4):
                for i in range(0, 3):
                    if macierz[i][k] == macierz[i + 1][k] and macierz[i][k] != 0:
                        macierz[i][k] = 2 * macierz[i][k]
                        macierz[i + 1][k] = 0
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
            for k in range(0, 4):
                for i in range(0, 3):
                    if macierz[3 - i][k] == macierz[2 - i][k] and macierz[3 - i][k] != 0:
                        macierz[3 - i][k] = 2 * macierz[3 - i][k]
                        macierz[2 - i][k] = 0
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
            for i in range(0, 4):
                for k in range(0,3):
                    if macierz[i][3-k] == macierz[i][2-k] and macierz[i][3-k] != 0:
                        macierz[i][3-k] = 2 * macierz[i][3-k]
                        macierz[i][2-k] = 0
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

from math import fabs

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




#for i in range(0, 4):
 #   macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
  #  while len(macierz[i]) < 4:
   #     macierz[i].insert(0, 0)




def lista4():
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


def lista3():
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





def column_to_list(matrix, size):
    work_list = []
    for column in range(0, size):
        for row in range(0, size):
            work_list.append(matrix[row][column])
    return work_list


def list_reversion(list_arg):
    list_arg = list(reversed(list_arg))
    return list_arg



def elements_movement(size, matrix, reversion=None):
    for index in range(0, size):
        if reversion is 'yes':
            matrix[index] = list(reversed(matrix[index]))
        matrix[index] = list(filter(lambda x: x > 0, matrix[index]))
        while len(matrix[index]) < size:
            matrix[index].append(0)
        if reversion is 'yes':
            matrix[index] = list(reversed(matrix[index]))






    for row in matrix:
        if reversion is 'yes':
            row = list_reversion(row)
        row = list(filter(lambda x: x > 0, row))
        while len(row) < size:
            row.append(0)
        if reversion is 'yes':
            row = list_reversion(row)







#def list_to_column(matrix, size, list):





matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

matrix_index_dictionaries_creation(4)

print(matrix)

matrix_addition(matrix, left)



elements_movement(4, matrix, 'yes')




print(matrix)









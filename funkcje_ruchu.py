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





def elements_in_row_movement(size, matrix, reversion=None):
    for index in range(0, size):
        if reversion is 'reversed':
            matrix[index] = list(reversed(matrix[index]))
        matrix[index] = list(filter(lambda x: x > 0, matrix[index]))
        while len(matrix[index]) < size:
            matrix[index].append(0)
        if reversion is 'reversed':
            matrix[index] = list(reversed(matrix[index]))

def condition_for_func_execution(matrix, condition_func, executed_func):
    pre_matrix = matrix
    condition_func
    if  not pre_matrix == condition_func:
        executed_func

matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

matrix_index_dictionaries_creation(4)

print(matrix)

matrix_addition(matrix, down)



elements_in_column_movement(4, matrix, 'reversed')



for i in matrix:
    print(i)
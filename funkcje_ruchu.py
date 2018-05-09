from math import fabs

def matrix_index_dictionaries_creation(size):
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

    global right
    global left
    global up
    global down


def columns_addition_left(matrix, size, direction):
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













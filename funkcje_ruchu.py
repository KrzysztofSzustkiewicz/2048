from math import fabs

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




def comparison_and_addition(a, b, c, d):
    if matrix[fabs(row + a)][fabs(column + b)] != 0:
        if matrix[fabs(row + a)][fabs(column + b)] == matrix[fabs(row + c)][fabs(column + d)]:
            matrix[fabs(row + a)][fabs(column + b)] = 2 * matrix[fabs(row +a)][fabs(column + b)]
            matrix[fabs(row + c)][fabs(column + d)] = 0





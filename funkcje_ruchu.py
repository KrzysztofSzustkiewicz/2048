from math import fabs

def columns_addition_left(matrix, size, direction):
    for row in range(0, size):
        for column in range(0, size - 1):
            if direction is 'left':
                if matrix[row][column] == matrix[row][column + 1] and matrix[row][column] != 0:
                   matrix[row][column] = 2 * matrix[row][column]
                   matrix[row][column + 1] = 0
            elif direction is 'right':
                if matrix[row][3 - column] == matrix[row][2 - column] and matrix[row][3 - column] != 0:
                    matrix[row][3 - column] = 2 * matrix[row][3 - column]
                    matrix[row][2 - column] = 0



#prawo
if matrix[row][3 - column] == matrix[row][2 - column] and matrix[row][3 - column] != 0:
    matrix[row][3 - column] = 2 * matrix[row][3 - column]
    matrix[row][2 - column] = 0

#lewo
if matrix[row][column] == matrix[row][column + 1] and matrix[row][column] != 0:
    matrix[row][column] = 2 * matrix[row][column]
    matrix[row][column + 1] = 0

#gora

if macierz[i][k] == macierz[i + 1][k] and macierz[i][k] != 0:
    macierz[i][k] = 2 * macierz[i][k]
    macierz[i + 1][k] = 0

#dol

if macierz[3 - i][k] == macierz[2 - i][k] and macierz[3 - i][k] != 0:
    macierz[3 - i][k] = 2 * macierz[3 - i][k]
    macierz[2 - i][k] = 0

def comparison_and_addition(a, b, c, d):
    if matrix[fabs(row +a)][fabs(column + b)] != 0:
        if matrix[fabs(row + a)][fabs(column + b)] == matrix[fabs(row + c)][fabs(column + d)]:
            matrix[fabs(row + a)][fabs(column + b)] = 2 * matrix[fabs(row +a)][fabs(column + b)]
            matrix[fabs(row + c)][fabs(column + d)] = 0





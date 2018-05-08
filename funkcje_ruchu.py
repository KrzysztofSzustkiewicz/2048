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

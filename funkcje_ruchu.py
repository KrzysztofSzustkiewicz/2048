for i in range(0, 4):
    for k in range(0, 3):
        if macierz[i][k] == macierz[i][k + 1] and macierz[i][k] != 0:
            macierz[i][k] = 2 * macierz[i][k]
            macierz[i][k + 1] = 0
for i in range(0, 4):
    macierz[i] = list(filter(lambda x: x > 0, macierz[i]))
    while len(macierz[i]) < 4:
        macierz[i].append(0)


def columns_addition_left(matrix, size):
    for row in range(0, size):
        for column in range(0, size - 1):
            r = row
            c = column
            if matrix[r][c] == matrix[r][c + 1] and matrix[r][c] != 0:
                matrix[r][c] = 2 * matrix[r][c]
                matrix[r][c + 1] = 0


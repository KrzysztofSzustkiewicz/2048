row=0
column=0

left={'first':column,'second':(column + 1),'third':row,'fourth':row}
right={'first':(3 - column),'second':(2 - column),'third':row,'fourth':row}
up={'first':column,'second':column,'third':row,'fourth':(row + 1)}
down={'first':column,'second':column,'third':(3 - row), 'fourth':(2 - row)}

def columns_addition(matrix,size,direction):
    for row in range(0, size):
        for column in range(0, size - 1):
                if matrix[direction['third']][direction['first']] == matrix[direction['fourth']][direction['second']] and matrix[direction['third']][direction['first']] != 0:
                    matrix[direction['third']][direction['first']] = 2 * matrix[direction['third']][direction['first']]
                    matrix[direction['fourthyy']][direction['second']] = 0
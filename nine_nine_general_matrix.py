import numpy as np

def constraints (matrix):
    for i in range(len(matrix)):
        #row_number = int(i / 16)
        row_number = int(i/81)
        #column_number = int((i % 16) / 4)
        column_number = int((i % 81) / 9)
        #value = int(i % 4) + 1
        value = int(i % 9) + 1
        #matrix[i][row_number * 4 + value - 1] = 1
        matrix[i][row_number * 9 + value - 1] = 1
        #matrix[i][column_number * 4 + value + 16 - 1] = 1
        matrix[i][column_number * 9 + value + 81 - 1] = 1
        #box_number_1 = int(row_number / 2)
        box_number_1 = int(row_number / 3)
        #box_number_2 = int(column_number / 2)
        box_number_2 = int(column_number / 3)
        #matrix[i][box_number_1 * 8 + box_number_2 * 4 + value + 32 -1] = 1
        matrix[i][box_number_1 * 27 + box_number_2 * 9 + value + 162 -1] = 1
        #matrix[i][row_number * 4 + column_number + 48] = 1
        matrix[i][row_number * 9 + column_number + 243] = 1
    return matrix

def give_constrained_matrix():
    #x = np.array([[0 for i in range(64)] for j in range(64)])
    x = np.array([[0 for i in range(324)] for j in range(729)])
    #x = [[0 for i in range(64)] for j in range(64)]
    x = constraints (x)
    return x

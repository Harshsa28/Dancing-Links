import numpy as np
import four_four_dlx
import four_four_general_matrix
from tabulate import tabulate

def cover (matrix, cover_rows):
    #we cover all columns which have 1 with row and all the rows which have 1s with those columns
    take_out_rows = set()
    for i in cover_rows:
        take_out_rows.add(i)
    take_out_columns = set()
    for i in cover_rows:
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                take_out_columns.add(j)
    for i in take_out_columns:
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                take_out_rows.add(j)
    take_out_rows = sorted(take_out_rows, reverse=True)
    take_out_columns = sorted(take_out_columns, reverse=True)
    #print("take out rows is :", take_out_rows)
    #print("take out columns is :", take_out_columns)
    for i in take_out_rows:
        matrix = np.delete(matrix, i, 0)
    for i in take_out_columns:
        matrix = np.delete(matrix, i, 1)
    #print('_' * 50)
    #print(len(matrix))
    #print(len(matrix[0]))
    #print('_' * 50)
    return [matrix, take_out_rows]


def final(take_out_rows, solution):
    x = [i for i in range(0,64) if i not in take_out_rows]
    for i in solution:
        row_number = int(x[i] / 16)
        column_number = int((x[i] % 16) / 4)
        value = int(x[i] % 4) + 1
        print(row_number , ' ; ', column_number, ' ; ', value)
        #print(x[i] ,end = ' ; ')
    #print('_' * 50)
    return

def solve():
    sudoku = 1000240302004002
    sudoku = [[1,0,0,0],
              [2,4,0,3],
              [0,2,0,0],
              [4,0,0,2]]
    sudoku = np.array([[1,0,0,0],[2,4,0,3],[0,2,0,0],[4,0,0,2]])
    sudoku = np.array([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    matrix = four_four_general_matrix.give_constrained_matrix()
    cover_rows = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] != 0:
                value = sudoku[i][j]
                #below, matrix is constrained matrix
                row_number_in_matrix = i * 16 + j * 4 + value - 1
                cover_rows.append(row_number_in_matrix)
                #matrix = cover_row (matrix, row_number_in_matrix)
    [matrix, take_out_rows] = cover (matrix, cover_rows)
    #print("printing covered matrix")
    #print(len(matrix))
    #print(len(matrix[0]))
    #print(matrix)
    #print(tabulate(matrix))
    solution = four_four_dlx.solve(matrix)
    #print("initial solution is :", solution)
    solution = sorted(solution)
    print("solution is  :", solution)
    take_out_rows = sorted (take_out_rows)
    #print("take out rows is :", take_out_rows)
    final (take_out_rows, solution)
    return



    
solve()

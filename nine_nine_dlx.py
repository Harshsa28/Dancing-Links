import nine_nine_matrix
import math #for infinity

O = {}
solution = []

def search (k, cols):
    global O
    #if cols["root"].right == cols["root"]:
    if cols[-1].right == cols[-1]:
        print_solution (k) 
        return
    c = choose_column (cols)  
    cover_column(c)
    r = c.down  
    while r != c:
        O[k] = r.name
        j = r.right 
        while j != r:
            cover_column(j.col)  #not sure whether its only 'j' or 'j.col'
            j = j.right
        search (k+1, cols)
        r.name = O[k]
        c = r.col
        j = r.left
        while j != r:
            uncover_column (j.col) #not sure whether it's only 'j' or 'j.col'
            j = j.left
        r = r.down
    uncover_column(c)
    return

def print_solution (k):
    global O
    global solution
    for i in range(0,k):
        solution.append(int(O[i].split(',')[0]))
        #print(O[i][0], end = ' ; ')
        #print(O[i].split(',')[0], end=' ; ')
    return

def choose_column(cols):
    s = math.inf
    #j = cols["root"].right
    j = cols[-1].right
    #while j != cols["root"]:
    while j != cols[-1]:
        if j.size < s:
            c = j
            s = j.size
        j = j.right
    return c

def cover_column(c):
    c.right.left = c.left
    c.left.right = c.right
    i = c.down
    while i != c:
        j = i.right
        while j != i:
            j.down.up = j.up
            j.up.down = j.down
            j.col.size -= 1
            j = j.right
        i = i.down
    return

def uncover_column(c):
    i = c.up
    while i != c:
        j = i.left
        while j != i:
            j.col.size += 1
            j.down.up = j
            j.up.down = j
            j = j.left
        i = i.up
    c.right.left = c
    c.left.right = c
    return

def solve(grid):
    global solution
    [grid1, cols, nodes] = nine_nine_matrix.give_values(grid)
    #print(cols)
    search(0, cols)
    return solution

grid1 = [[0,0,1,0,1,1,0],
          [1,0,0,1,0,0,1],
          [0,1,1,0,0,1,0],
          [1,0,0,1,0,0,0],
          [0,1,0,0,0,0,1],
          [0,0,0,1,1,0,1]]

grid2 = [[1,1,0,0,0,0],
        [0,0,0,0,1,1],
        [0,0,0,1,1,0],
        [1,1,1,0,0,0],
        [0,0,1,1,0,0],
        [0,0,0,1,1,0],
        [1,0,1,0,1,1]]

grid3 = [[1,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,1,0,1],
        [0,0,1,0,1,1,0],
        [0,1,1,0,0,1,1],
        [0,1,0,0,0,0,1]]




#solve(grid1)















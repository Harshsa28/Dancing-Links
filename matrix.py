class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.col = None

class Column_Node:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.col = None  #not sure why this needs a column object



def initialize_columns(grid):
    cols = {}
    num_rows = len(grid)
    num_cols = len(grid[0])
    cols["root"] = Column_Node(0, "root")
    cols["root"].left = cols["root"]
    cols["root"].right = cols["root"]
    for i in range(num_cols):
        name = chr(65+i)
        size = 0
        for j in range(num_rows):
            if grid[j][i] == 1:
                size += 1
        cols[name] = Column_Node(size, name)
        if name == chr(65+0):
            cols["root"].right = cols[name]
        if name == chr(65+num_cols-1):
            cols["root"].left = cols[name]
    return cols

def initialize_nodes(grid):
    nodes = {}
    num_rows = len(grid)
    num_cols = len(grid[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                nodes[chr(65+i)+chr(65+j)] = Node(chr(65+i)+chr(65+j))
    return nodes

def parameterize_columns(grid, cols, nodes):
    num_rows = len(grid)
    num_cols = len(grid[0])
    required_range = [x for x in cols if x != "root"]
    for i in required_range:
        if i == chr(65+0):
            cols[i].left = cols["root"]
        else:
            cols[i].left = cols[chr(ord(i)-1)]

        if i == chr(65+num_cols-1):
            cols[i].right = cols["root"]
        else:
            cols[i].right = cols[chr(ord(i)+1)]

        cols[i].col = cols[i]

        number_of_column = ord(i)-65
        for j in range(num_rows-1, -1, -1):
            if grid[j][number_of_column] == 1:
                cols[i].up = nodes[chr(65+j)+chr(65+number_of_column)]
                break
        if cols[i].up is None:
            cols[i].up = cols[i]

        for j in range(num_rows):
            if grid[j][number_of_column] == 1:
                cols[i].down = nodes[chr(65+j)+chr(65+number_of_column)]
                break
        if cols[i].down is None:
            cols[i].down = cols[i]
        
    return cols

def parameterize_nodes(grid, cols, nodes):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in nodes:
        number_of_row = ord(i[0])-65
        number_of_col = ord(i[1])-65
        for j in range(num_cols):
            required_col = number_of_col - j - 1
            if required_col < 0:
                required_col = num_cols + required_col
            if grid[number_of_row][required_col] == 1:
                nodes[i].left = nodes[chr(65+number_of_row)+chr(65+required_col)]
                break
        
        for j in range(num_cols):
            required_col = number_of_col + j + 1
            if required_col >= num_cols:
                required_col = required_col - num_cols
            if grid[number_of_row][required_col] == 1:
                nodes[i].right = nodes[chr(65+number_of_row)+chr(65+required_col)]
                break

        for j in range(number_of_row-1, -1, -1):
            if grid[j][number_of_col] == 1:
                nodes[i].up = nodes[chr(65+j)+chr(65+number_of_col)]
                break
        if nodes[i].up is None:
            nodes[i].up = cols[chr(65+number_of_col)]

        for j in range(number_of_row+1, num_rows):
            if grid[j][number_of_col] == 1:
                nodes[i].down = nodes[chr(65+j)+chr(65+number_of_col)]
                break
        if nodes[i].down is None:
            nodes[i].down = cols[chr(65+number_of_col)]

        nodes[i].col = cols[chr(65+number_of_col)]
    
    return nodes





'''
columns = initialize_columns (matrix)
nodes = initialize_nodes (matrix)
columns = parameterize_columns(matrix, columns, nodes)
nodes = parameterize_nodes(matrix, columns, nodes)
'''


def print_column(cols, nodes):
    for i in cols:
        if i != "root":
            print("col is :", i)
            print("name of col is :", cols[i].name)
            print("size of col is :", cols[i].size)
            print("left is :", cols[i].left.name)
            print("right is :", cols[i].right.name)
            print("up is :", cols[i].up.name)
            print("down is :", cols[i].down.name)

def print_nodes(cols, nodes):
    for i in nodes:
        print("node is :", i)
        print("left is :", nodes[i].left.name)
        print("right is :", nodes[i].right.name)
        print("up is :", nodes[i].up.name)
        print("down is :", nodes[i].down.name)
        print("col is :", nodes[i].col.name)

        
def give_values (matrix):
    columns = initialize_columns(matrix)
    nodes = initialize_nodes(matrix)
    columns = parameterize_columns(matrix, columns, nodes)
    nodes = parameterize_nodes(matrix, columns, nodes)
    return [matrix, columns, nodes]

'''
matrix = [[0,0,1,0,1,1,0],
          [1,0,0,1,0,0,1],
          [0,1,1,0,0,1,0],
          [1,0,0,1,0,0,0],
          [0,1,0,0,0,0,1],
          [0,0,0,1,1,0,1]]
'''



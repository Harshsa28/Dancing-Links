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
    #cols["root"] = Column_Node(0, "root")
    cols[-1] = Column_Node(0, -1)
    #cols["root"].left = cols["root"]
    cols[-1].left = cols[-1]
    #cols["root"].right = cols["root"]
    cols[-1].right = cols[-1]
    for i in range(num_cols):
        #name = chr(65+i)
        name = i
        size = 0
        for j in range(num_rows):
            if grid[j][i] == 1:
                size += 1
        cols[name] = Column_Node(size, name)
        #if name == chr(65+0):
        if name == 0:
            #cols["root"].right = cols[name]
            cols[-1].right = cols[name]
        #if name == chr(65+num_cols-1):
        if name == num_cols-1:
            #cols["root"].left = cols[name]
            cols[-1].left = cols[name]
    return cols

def initialize_nodes(grid):
    nodes = {}
    num_rows = len(grid)
    num_cols = len(grid[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                #nodes[chr(65+i)+chr(65+j)] = Node(chr(65+i)+chr(65+j))
                #nodes[[i,j]] = Node([i,j]) 
                nodes[str(i)+','+str(j)] = Node(str(i)+','+str(j))
    return nodes

def parameterize_columns(grid, cols, nodes):
    num_rows = len(grid)
    num_cols = len(grid[0])
    #required_range = [x for x in cols if x != "root"]
    required_range = [x for x in cols if x != -1]
    for i in required_range:
        #if i == chr(65+0):
        if i == 0:
            #cols[i].left = cols["root"]
            cols[i].left = cols[-1]
        else:
            #cols[i].left = cols[chr(ord(i)-1)]
            cols[i].left = cols[i-1]
        #if i == chr(65+num_cols-1):
        if i == num_cols-1:
            #cols[i].right = cols["root"]
            cols[i].right = cols[-1]
        else:
            #cols[i].right = cols[chr(ord(i)+1)]
            cols[i].right = cols[i+1]

        cols[i].col = cols[i]

        #number_of_column = ord(i)-65
        number_of_column = i

        for j in range(num_rows-1, -1, -1):
            if grid[j][number_of_column] == 1:
                #cols[i].up = nodes[chr(65+j)+chr(65+number_of_column)]
                #cols[i].up = nodes[[j, number_of_column]]
                cols[i].up = nodes[str(j)+','+str(number_of_column)]
                break
        if cols[i].up is None:
            cols[i].up = cols[i]

        for j in range(num_rows):
            if grid[j][number_of_column] == 1:
                #cols[i].down = nodes[chr(65+j)+chr(65+number_of_column)]
                #cols[i].down = nodes[[j, number_of_column]]
                cols[i].down = nodes[str(j)+','+str(number_of_column)]
                break
        if cols[i].down is None:
            cols[i].down = cols[i]
        
    return cols

def parameterize_nodes(grid, cols, nodes):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in nodes:
        #number_of_row = ord(i[0])-65
        #number_of_row = i[0]
        number_of_row = int(i.split(",")[0])
        #number_of_col = ord(i[1])-65
        #number_of_col = i[1]
        number_of_col = int(i.split(",")[1])
        for j in range(num_cols):
            required_col = number_of_col - j - 1
            if required_col < 0:
                required_col = num_cols + required_col
            if grid[number_of_row][required_col] == 1:
                #nodes[i].left = nodes[chr(65+number_of_row)+chr(65+required_col)]
                #nodes[i].left = nodes[[number_of_row, required_col]]
                nodes[i].left = nodes[str(number_of_row)+','+str(required_col)]
                break
        
        for j in range(num_cols):
            required_col = number_of_col + j + 1
            if required_col >= num_cols:
                required_col = required_col - num_cols
            if grid[number_of_row][required_col] == 1:
                #nodes[i].right = nodes[chr(65+number_of_row)+chr(65+required_col)]
                #nodes[i].right = nodes [ [number_of_row, required_col]]
                nodes[i].right = nodes[str(number_of_row)+','+str(required_col)]
                break

        for j in range(number_of_row-1, -1, -1):
            if grid[j][number_of_col] == 1:
                #nodes[i].up = nodes[chr(65+j)+chr(65+number_of_col)]
                #nodes[i].up = nodes[[j, number_of_col]]
                nodes[i].up = nodes[str(j)+','+str(number_of_col)]
                break
        if nodes[i].up is None:
            #nodes[i].up = cols[chr(65+number_of_col)]
            nodes[i].up = cols[number_of_col]

        for j in range(number_of_row+1, num_rows):
            if grid[j][number_of_col] == 1:
                #nodes[i].down = nodes[chr(65+j)+chr(65+number_of_col)]
                #nodes[i].down = nodes[[j, number_of_col]]
                nodes[i].down = nodes[str(j)+','+str(number_of_col)]
                break
        if nodes[i].down is None:
            #nodes[i].down = cols[chr(65+number_of_col)]
            nodes[i].down = cols[number_of_col]

        #nodes[i].col = cols[chr(65+number_of_col)]
        nodes[i].col = cols[number_of_col]
    
    return nodes





'''
columns = initialize_columns (matrix)
nodes = initialize_nodes (matrix)
columns = parameterize_columns(matrix, columns, nodes)
nodes = parameterize_nodes(matrix, columns, nodes)
'''


def print_column(cols, nodes):
    for i in cols:
        if i != -1:
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
    #print_column(columns, nodes)
    #print_nodes(columns, nodes)
    return [matrix, columns, nodes]


matrix = [[0,0,1,0,1,1,0],
          [1,0,0,1,0,0,1],
          [0,1,1,0,0,1,0],
          [1,0,0,1,0,0,0],
          [0,1,0,0,0,0,1],
          [0,0,0,1,1,0,1]]

#print(give_values(matrix))

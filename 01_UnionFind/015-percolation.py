# WEIGHTED QUICK UNION WITH PATH COMPRESSION

import random

class WQUPC:
    def __init__(self, n: int):
        # n: number of points in the set. 0 to n-1 
        self.n = n
        self.data = [i for i in range(n)]
        self.sz = [0 for i in range(n)]


    def check_valid(self,a,b):
        # verify if inputs are valid 
        if a<0 or b<0 or a>(self.n-1) or b>(self.n-1):
            print(f"Invalid input {a} or {b}")
            raise ValueError
    
    def find_root(self, a):
        while a != self.data[a]:
            a = self.data[a]
            #path compression (1-pass variant) 
            self.data[a] = self.data[self.data[a]]
        return a 


    def union(self, a,b): 
        # connect a and b
        self.check_valid(a,b)
        p = self.find_root(a)
        q = self.find_root(b)

        # Weighted connection
        if self.sz[p] > self.sz[q]:
            self.data[q] = p
            self.sz[q] +=self.sz[q]
        else: 
            self.data[p] = q
            self.sz[p] +=self.sz[p]


    def print_data(self):
        print(self.data)
    
    def connected(self,a,b):
        #checks if a  and b are connected
        self.check_valid(a,b)

        p = self.find_root(a)
        q = self.find_root(b)
        if p==q:
            return 1
        else: 
            return 0

class gridSolver():

    def __init__(self, n: int):
        self.n = n                                                  # grid size
        self.total_elem = (n**2) +2                                 #includes start node and end node
        self.grid = [[0 for j in range(n)] for i in range(n)]       # n by n grid
        self.start_node_index = (n**2)                              # set start node
        self.end_node_index = (n**2) +1                             # set end node

        self.closed_cells = [i for i in range(n**2)]
        
        # initiate wqupc
        self.qu = WQUPC(self.total_elem)

        #connect first row to start node
        for i in range(n):
            self.qu.union(self.start_node_index, i)

        # connect last row to end node
        for i in range(n):
            self.qu.union(self.end_node_index, (n*(n-1)) + i)

    def get_index(self, node):
        # converts x,y on grid to index
        return self.n * node[0] + node[1]

    def get_node(self, index):
        # converts index to grid x,y
        return [index//self.n, index%self.n]

    def open_cell(self):

        # randomly open a closed cell
        opened_cell = random.choice(self.closed_cells)
        self.closed_cells.remove(opened_cell)
        index_x,index_y = self.get_node(opened_cell)
        self.grid[index_x][index_y] = 1

        # get neighbours of the opened cell
        neighbours = self.get_neighbour([index_x,index_y])

        # if neighbours are also open, then cells can be connected
        for neighbour_node in neighbours:
            index_neighbour_node = self.get_index(neighbour_node)
            if index_neighbour_node not in self.closed_cells:
                self.qu.union(opened_cell, index_neighbour_node)

    def runGrid(self):
        # solve the grid

        i=0

        # loop until the grid is connected
        while self.qu.connected(self.start_node_index, self.end_node_index) != 1: 
            #open cell
            self.open_cell()
            i+=1

        # returns the iteration at which grid percolated
        return i

    def get_neighbour(self, node):
        #get neighbours 

        index_x,index_y = node[0], node[1]
        neighbours = []
        if index_x >0 :
            # left neighbour exists
            neighbours.append([index_x-1, index_y])
        if index_x < self.n-1:
            # right neighbour exists
            neighbours.append([index_x+1, index_y])

        if index_y >0 :
            # top neighbour exists
            neighbours.append([index_x, index_y-1])
        if index_y < self.n-1:
            # bottom neighbour exists
            neighbours.append([index_x, index_y+1])

        # returns all valid neighbours as a list
        return neighbours

class percolation():
    # Runs Percolation experiement

    def __init__(self, n:int, iteration: int = 10):
        self.n = n
        self.p = []

        # Run grid iteration times
        for i in range(iteration):
            # init grid
            grid = gridSolver(n)

            # Solve grid
            self.p.append(grid.runGrid())

            print(f"completed {i+1}/{iteration}")
        
        # Calculate p_star over all the iterations 
        self.p_star = sum(self.p ) / len(self.p )/self.n**2
        print(f"pstar = {self.p_star } for percolation on grid of {n}*{n} with {iteration} iterations.")


### MAIN CODE STARTS HERE ###

# check test cases for grid solver: 
p = gridSolver(5)
assert(p.get_index([4,4]) == 24)
assert(p.get_neighbour([0,1]) == [[1, 1], [0, 0], [0, 2]])
assert(p.get_node(24)==[4, 4])
assert(p.get_neighbour([4,4])==[[3, 4], [4, 3]])


# check test cases for WQUPC: 
n = 10
uf = WQUPC(10)
connections=[(5,0),(6,0),(2,1),(7,1),(8,3),(8,9), (4,3)]
for a,b in connections:
    uf.union(a,b)
assert(uf.connected(6,2)==0)
uf.union(6,2)
assert(uf.connected(6,2)==1)


# RUN percolation Experiement
p = percolation(n=20, iteration=500)
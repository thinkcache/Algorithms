from typing import List
from operator import add
import copy

class board():
    "Defines the state of the board at a given point."

    def __init__(self, config: List, debug=False):
        "config = [][] 2 dim list"
        "always n by n"
        self.debug =debug
        self.config = config
        self.dim = len(config)

    def getConfig(self):
        return self.config

    def printBoard(self):
        for i in range(self.dim):
            print(" ".join([str(j) for j in self.config[i]]))

    def dimensions(self):
        return self.dim
    
    def hamming(self):
        ideal_board = self.getGoal()
        return sum([sum([self.config[i][j]!=ideal_board[i][j] for j in range(self.dim)]) for i in range(self.dim)])

    def manhattan(self):
        ideal_board = self.getGoal()
        board_repr = {}
        ideal_board_repr = {}
        for i in range(self.dim):
            for j in range(self.dim):
                board_repr[self.config[i][j]] = (i,j)
        for i in range(self.dim):
            for j in range(self.dim):
                ideal_board_repr[ideal_board[i][j]] = (i,j)
        
        man_dist = {}
        for i in range(self.dim**2):
            dist_x = board_repr[i][0] - ideal_board_repr[i][0]
            dist_y = board_repr[i][1] - ideal_board_repr[i][1]
            if dist_x<0:
                dist_x = - dist_x
            if dist_y<0:
                dist_y = - dist_y
            man_dist[i] = dist_x + dist_y
        
        return sum([man_dist[i] for i in range(self.dim**2)])

    def getGoal(self):
        c = 1
        board = [] 
        for i in range(self.dim):
            board.append(list( map(add, [c]*self.dim, range(self.dim)) ))
            c = c + self.dim
        board[self.dim-1][ self.dim-1] = 0
        return board

    def isGoal(self):
        goal = self.getGoal()
        return goal == self.config
        
    def __eq__(self, other): 
        if not isinstance(other, board):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.config == other.config

    def neighbors(self):
        # identify position of zero
        pos_identified = False
        for i in range(self.dim):
            for j in range(self.dim):
                if self.config[i][j] == 0:
                    pos0=(i,j)
                    pos_identified = True
                    break
            if pos_identified == True: 
                break

        # possible movements identification
        up = True
        down = True
        left = True
        right = True

        if pos0[0] == 0: 
            up = False
        elif pos0[0] == self.dim-1: 
            down = False

        if pos0[1] == 0: 
            left = False
        elif pos0[1] == self.dim-1: 
            right = False
        
        # identify swaps 
        swaps = []
        if down:
            # print("down")
            swaps.append((pos0[0]+1, pos0[1]))
        if up:
            # print("up")
            swaps.append((pos0[0]-1, pos0[1]))
        if right:
            # print("right")
            swaps.append((pos0[0], pos0[1]+1))
        if left:
            # print("left")
            swaps.append((pos0[0], pos0[1]-1))

        # perform swap
        neighbour_configs = []
        for i, swap_pos in enumerate(swaps):
            # print(f"swapping {swap_pos} and {pos0}")
            
            config2 = copy.deepcopy(self.config)
            config2[swap_pos[0]][swap_pos[1]], config2[pos0[0]][pos0[1]] = config2[pos0[0]][pos0[1]], config2[swap_pos[0]][swap_pos[1]]
            neighbour_configs.append(config2)
        return [board(config) for config in neighbour_configs]


##TEST CASES
print("Initiating unitTest Cases")

# ideal board b0 and b1
b0 = board(config=[[1,2,3],[4,5,6],[7,8,0]])
b1 = board(config=[[1,2,3],[4,5,6],[7,8,0]])
b3 = board(config=[[1,0,2],[3,4,5],[6,7,8]])
# b0.printBoard()
assert b0.hamming() == 0
assert b0.manhattan() == 0

assert b0.isGoal() == True
assert b3.isGoal() == False
assert (b0==b1) == True
assert (b0==b3) == False
comp1= [[[1, 4, 2], [3, 0, 5], [6, 7, 8]], [[1, 2, 0], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]
assert  sum([1  for i in b3.neighbors() if i.getConfig() in comp1]) ==3
print("Passed all UnitTests")



class minPQ():
    """
    Minimum Priority Queue
    """
    def __init__(self, debug=False):
        self.q = []
        self.debug = debug

    def insert(self, b: board): 
        if self.debug == True: 
            print(f"Inserting: {b}")

        self.q.append(b)

    def isEmpty(self):
        return len(self.q) == 0 

    def pop(self): 
        if len(self.q) == 0 :
            return None
        

        # calculate priority of node
        pv = []
        for i in range(len(self.q)):
            pv.append(self.q[i][0].manhattan() + self.q[i][1])
        # print(pv)

        # identify lowest priority
        m=0
        for i in range(len(self.q)):
            if pv[i] < pv[m]:
                m = i
            
        value = self.q[m]
        del self.q[m]
        return value
    

### Solving 8Puzzle  ###

#setting up MinPQ

pq = minPQ()

# b0 = board(config=[[1,2,3],[4,5,6],[7,0,8]])
b0 = board(config=[[0,1,3],[4,2,5],[7,8,6]])
# nodes of the PQ
# (board, number of moves made to reach the board, previous search node)

# insert initial node
pq.insert((b0, 0, None))

while True: 
    pop = pq.pop()
    pop[0].printBoard()
    print("")
    if pop[0].isGoal():
        print(f"Optimal path is with {pop[1]} moves")

        break

    neighbourBoards = (pop[0].neighbors())
    moves = pop[1] +1
    for b in neighbourBoards: 
        pq.insert((b, moves, pop[0]))
 
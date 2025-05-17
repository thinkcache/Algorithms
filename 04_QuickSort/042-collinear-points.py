# Identify collinear points (atleast 4)

import numpy as np

#variables
min_points = 4

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope(self, p2): 
        if p2.x == self.x:
            return np.inf
        slope = (p2.y - self.y) / (p2.x - self.x)
        return slope

    

set1 = [[10000  ,0    ],
        [0  ,10000],
        [3000   ,7000],
        [7000   ,3000],
        [20000  ,21000],
        [3000   ,4000],
        [14000  ,15000],
        [6000   ,7000] ]

set1_p = [Point(i[0], i[1]) for i in set1]

l = len(set1_p)
slope_list = []

# calculate slope
for index_i, p in enumerate(set1_p):
    slope_sublist = []
    for index_j, p2 in enumerate(set1_p):
        if index_i != index_j:
            slope_sublist.append((index_j, p.slope(p2)))
    
    slope_list.append(slope_sublist)

set_cpoints = []
# sort by clope
for i in range(l): 

    slope_list[i] = sorted(slope_list[i], key = lambda x:[x[1]] )
    print(slope_list[i])
    for j in range(len(slope_list[i])-2):
        
        if slope_list[i][j][1] ==  slope_list[i][j+1][1] and slope_list[i][j][1] ==  slope_list[i][j+2][1]:
            set_temp  = {i , slope_list[i][j][0], slope_list[i][j+1][0], slope_list[i][j+2][0]}
            if set_temp not in set_cpoints:
                set_cpoints.append({i, slope_list[i][j][0], slope_list[i][j+1][0], slope_list[i][j+2][0]})

print(set_cpoints)
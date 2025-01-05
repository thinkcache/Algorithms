# WEIGHTED QUICK UNION WITH PATH COMPRESSION

class WQUPC:
    def __init__(self, n: int):
        # n: number of points in the set. 0 to n-1 
        self.n = n
        self.data = [i for i in range(n)]
        self.sz = [0 for i in range(n)]


    def check_valid(self,a,b):
        # verify if inputs are valid 
        if a<0 or b<0 or a>(self.n-1) or b>(self.n-1):
            print("Invalid input")
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

        # Weighted 
        if self.sz[p] > self.sz[q]:
            self.data[q] = p
            self.sz[q] +=self.sz[q]
        else: 
            self.data[p] = q
            self.sz[p] +=self.sz[p]


    def print_data(self):
        print(self.data)
    
    def connected(self,a,b):
        self.check_valid(a,b)

        p = self.find_root(a)
        q = self.find_root(b)
        if p==q:
            print(f"{a} and {b} are connected.")
        else: 
            print(f"{a} and {b} are NOT connected.")





n = 10
uf = WQUPC(10)
connections=[(5,0),(6,0),(2,1),(7,1),(8,3),(8,9), (4,3)]
for a,b in connections:
    uf.union(a,b)
uf.print_data()
uf.connected(6,2)
uf.union(6,2)
uf.print_data()
uf.connected(6,2)

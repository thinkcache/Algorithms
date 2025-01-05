

class UnionFind:
    def __init__(self, n: int):
        # n: number of points in the set. 0 to n-1 
        self.n = n
        self.data = [{i} for i in range(n)]


    def check_valid(self,a,b):
        # verify if inputs are valid 
        if a<0 or b<0 or a>(self.n-1) or b>(self.n-1):
            print("Invalid input")
            raise ValueError
    
    def union(self, a,b): 
        # connect a and b
        
        self.check_valid(a,b)

        
        set1 = None
        set2 = None

        for s in self.data:
            if a in s:
                set1=s
            if b in s:
                set2=s

        if set1 != set2:
            set1.update(set2)
            self.data.remove(set2)
        elif set1==set2: 
            pass
        else: 
            print("either element not found.")

    def print_data(self):
        print(self.data)
    
    def connected(self,a,b):
        self.check_valid(a,b)
        for s in self.data:
            if a in s and b in s: 
                print(f"{a} and {b} are connected.")
                return 1

        print(f"{a} and {b} are NOT connected.")




n = 10
uf = UnionFind(10)
connections=[(1,4),(1,5),(2,3),(6,3),(3,7),(8,9)]
for a,b in connections:
    uf.union(a,b)
uf.print_data()
uf.connected(1,2)
uf.union(1,2)
uf.connected(1,2)

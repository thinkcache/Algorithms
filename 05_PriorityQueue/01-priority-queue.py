class minPQ():
    """
    Minimum Priority Queue
    """
    def __init__(self, debug=False):
        self.q = []
        self.debug = debug

    def insert(self, d): 
        if self.debug == True: 
            print(f"Inserting: {d}")

        self.q.append(d)

    def isEmpty(self):
        return len(self.q) == 0 

    def pop(self): 
        if len(self.q) == 0 :
            return None
        m=0
        for i in range(len(self.q)):
            if self.q[i] < self.q[m]:
                m = i
            
        value = self.q[m]
        del self.q[m]
        return value

q = minPQ(debug=True)
q.insert(1)
q.insert(2)
q.insert(5)
q.insert(-1)
q.insert(-100)

while not q.isEmpty():
    pop = q.pop()
    print(f"Popped: {pop}")

print("Check if PQ is empty")
print(q.isEmpty())

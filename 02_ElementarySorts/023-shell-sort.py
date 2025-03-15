lst = [9,3,1,5,4,8,10,2,6,7]

class shellSort():
    
    def __init__(self, lst, gap = -1, debug=False):
        self.lst = lst
        self.debug = debug
        if gap == -1:
            self.gap = len(self.lst)//2
        else: 
            self.gap = gap
        print(f"Gap is initialized as {self.gap}")

    def run_sort(self):
        
        while self.gap >0:
            if self.debug:
                print(f"New gap ={self.gap}")
            
            for i in range(self.gap,len(self.lst)):
                j = i
                mv_index = i
                
                while j>= self.gap:
                    j = j- self.gap
                
                    if self.lst[mv_index] < self.lst[j]: 
                        self.lst[mv_index], self.lst[j] = self.lst[j], self.lst[mv_index]
                        if self.debug:
                            print(f"sorted {mv_index},{j}, {self.lst}")
                        mv_index = j
                    
                    else:
                        break

            self.gap = self.gap //2 

        return self.lst
    
sort = shellSort(lst, debug=True)
print(sort.run_sort())

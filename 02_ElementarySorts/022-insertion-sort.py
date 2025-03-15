lst = [9,3,1,5,4,8,10,2,6,7]

class insertionSort():
    
    def __init__(self, lst, debug=False):
        self.lst = lst
        self.debug = debug

    def run_sort(self):
        for i in range(1,len(self.lst)):
            select = i
            for j in range(i-1,-1,-1):
                if self.lst[select]< self.lst[j]:
                    self.lst[select], self.lst[j] = self.lst[j], self.lst[select]
                    if self.debug:
                        print(f"{i} iter, {j} back loop: {self.lst}")
                    select = j      
                else:
                    break
        return self.lst
    
sort = insertionSort(lst, debug=True)
print(sort.run_sort())

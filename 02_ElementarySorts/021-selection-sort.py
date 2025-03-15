lst = [9,3,1,5,4,8,10,2,6,7]

class selectionSort():
    
    def __init__(self, lst, debug=False):
        self.lst = lst
        self.debug = debug

    def run_sort(self):
        for i in range(len(self.lst)):
            min_index = i
            for j in range(i+1, len(self.lst)):
                if self.lst[j] < self.lst[min_index]:
                    min_index = j

            if i!=j:
                self.lst[i], self.lst[min_index] = self.lst[min_index], self.lst[i]
            
            if self.debug:
                print(f"{i} iter. List is {self.lst}")
        return self.lst

sort = selectionSort(lst, debug=True)
print(sort.run_sort())



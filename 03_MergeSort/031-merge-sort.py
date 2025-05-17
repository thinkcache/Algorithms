import random 

def shuffle_seq(len=10):
    lst = [i for i in range(len)]
    for i in range(1,len):
        r = random.randrange(0,i)
        lst[r], lst[i] = lst[i], lst[r]
    return lst


class mergeSort():
    """
    Bottom up approach
    """
    def __init__(self, lst, debug=False):
        self.lst = lst
        self.debug = debug
        self.l = len(self.lst)

    def run_sort(self):
        #1st iter
        n=1
        while n<self.l:
            n=n*2
            for i in range(0,self.l,n):
                self.merge(i,int(i+(n/2)),i+n)
            if self.debug:
                print(f"{n} : {self.lst}")
            
        return self.lst

    def merge(self, l, m, r):

        #copy content into aux arr
        l_arr = [self.lst[i] for i in range(l,m) if i <self.l ]
        r_arr = [self.lst[i] for i in range(m,r) if i <self.l ]

        n1=len(l_arr) #len of 1st subarr
        n2=len(r_arr) #len of 2nd subarr

        # print(l_arr, r_arr)

        i = 0 #index for l_arr
        j = 0 #index for r_arr
        k = l #index for main arr

        while i<n1 and j<n2:
            if l_arr[i] <= r_arr[j]:
                self.lst[k] = l_arr[i]
                k+=1
                i+=1
            else: 
                self.lst[k] = r_arr[j]
                k+=1
                j+=1

        while i<n1:
            self.lst[k] = l_arr[i]
            k+=1
            i+=1
        
        while j<n2:
            self.lst[k] = r_arr[j]
            k+=1
            j+=1
        

print("Unsorted list is: ")
lst = shuffle_seq(30)
print(lst)

sort = mergeSort(lst, debug=True)
lst = (sort.run_sort())

print("Sorted list is: ")
print(lst)

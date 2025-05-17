import random 

def shuffle_seq(len=10):
    lst = [i for i in range(len)]
    for i in range(1,len):
        r = random.randrange(0,i)
        lst[r], lst[i] = lst[i], lst[r]
    return lst

lst1 = (shuffle_seq(10))
print(f"Original list: {lst1}")


def partition(lst, start, end):
    pivot = lst[end]
    i = start-1
    for j in range(start, end):
        if lst[j] <= pivot:
            i+=1
            lst[i], lst[j] = lst[j],lst[i]

            print(f"Swap {i} and {j}, lst new = {lst}")

    lst[i+1] , lst[end] = lst[end], lst[i+1]
    return(i+1)



def sort(lst, start=0, end=-1):
    if end == -1:
        end = len(lst)-1

    if start >= end:
        return None
    pivot = partition(lst, start, end)

    sort(lst,start,pivot-1)
    sort(lst,pivot+1,end ) 
    return(pivot)
sort(lst1)
print(lst1)
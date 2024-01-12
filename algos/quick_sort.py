def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)
    

test = [5, 3, 8, 1, 3]
print(qsort(test))
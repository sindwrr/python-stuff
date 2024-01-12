def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif n == 1 or n == 2:
        return n
    return n * factorial(n - 1)
    
    
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
    
arr = [4, 7, 6, 2, 1]
print(max(arr))
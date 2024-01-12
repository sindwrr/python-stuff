def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid
    
    return None

list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item = 17

ans = binarySearch(list, item)
print(ans)
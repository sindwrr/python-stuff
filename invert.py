def invert(str):
    inv = ''
    for i in range(len(str)):
        inv += str[len(str) - i - 1]
    return inv
    

s = input("Enter a string: ")
print(f"String flipped: {invert(s)}")
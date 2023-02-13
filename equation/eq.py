from cmath import sqrt


def solve(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        print("No roots!")
        return 0
    elif D == 0:
        x = - b / (2 * a)
        print(f"X = {x}")
        return 1
    else:
        x1 = (- b + sqrt(D)) / (2 * a)
        x2 = (- b - sqrt(D)) / (2 * a)
        print(f"X1 = {x1}\nX2 = {x2}")
        return 2

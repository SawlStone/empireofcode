from math import acos, degrees
def angles(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return [0, 0, 0]
    else:
        alpha = round(degrees(acos((b*b+c*c-a*a)/(2*b*c))))
        beta = round(degrees(acos((a*a+c*c-b*b)/(2*a*c))))
        gamma = round(degrees(acos((a*a+b*b-c*c)/(2*a*b))))
        return sorted([alpha, beta, gamma])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

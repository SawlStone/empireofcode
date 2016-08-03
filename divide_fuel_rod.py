# https://github.com/Empire-of-Code-Puzzles/checkio-empire-divide-fuel-rod

def disjoint(number):
    n = [(i ** 2 + i)//2 for i in range(1, 1000)]
    for t in range(len(n)):
        u = []
        for e in n[t:]:
            u.append(e)
            if number == sum(u):
                return u
    return []


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disjoint(64) == [15, 21, 28], "1st example"
    assert disjoint(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert disjoint(225) == [105, 120], "1st example"
    assert disjoint(882) == [], "1st example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

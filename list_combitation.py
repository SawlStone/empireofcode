# https://github.com/Empire-of-Code-Puzzles/checkio-empire-list-combination

def list_combination(list1, list2):
    return [j for i in list(zip(list1, list2)) for j in i]

if __name__ == '__main__':
    assert list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6], "First"
    assert list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2], "Second"

    print("All set? Click \"Check\" to review your code and earn rewards!")

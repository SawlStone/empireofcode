# https://github.com/Empire-of-Code-Puzzles/checkio-empire-count-inversion

def count_inversion(sequence):
    my_list = list(sequence)
    temp = 0
    step = 0
    while temp < len(my_list):
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                step += 1
        temp += 1
    return step


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

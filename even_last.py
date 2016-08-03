# https://github.com/Empire-of-Code-Puzzles/checkio-empire-even-last

def even_last(array):
    return 0 if not array else sum(array[::2]) * array[-1]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"

    print("Use 'Check' to earn sweet rewards!")

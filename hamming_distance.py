# https://github.com/Empire-of-Code-Puzzles/checkio-empire-hamming-distance

def hamming(n, m):
    return sum([int(i[0]) ^ int(i[1]) for i in zip(format(n, 'b').zfill(32), format(m, 'b').zfill(32))])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hamming(117, 17) == 3, "First example"
    assert hamming(1, 2) == 2, "Second example"
    assert hamming(16, 15) == 5, "Third example"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

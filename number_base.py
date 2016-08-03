# https://github.com/Empire-of-Code-Puzzles/checkio-empire-number-radix

def convert(str_number, radix):
    try:
        return int(str_number, radix)
    except:
        return -1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")
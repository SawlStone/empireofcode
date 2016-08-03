# https://github.com/Empire-of-Code-Puzzles/checkio-empire-crystal-row

def check_line(line):
    if len(set(line)) == 1:
        return False
    return True if len(set(line[1::2])) + len(set(line[::2])) == 2 else False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_line(["X", "Z", "X"]) == True
    assert check_line(["X", "Z", "X", "X"]) == False
    assert check_line(["X", "Z"]) == True
    assert check_line(["Z", "X"]) == True
    assert check_line(["Z", "X", "Z", "X", "Z", "Z", "X"]) == False

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

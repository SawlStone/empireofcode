# https://github.com/Empire-of-Code-Puzzles/checkio-empire-boolean-algebra

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == 'conjunction':		return x and y
    elif operation == 'disjunction':	return x or y
    elif operation == 'implication':	return (1 - x) | y
    elif operation == 'exclusive':		return x ^ y
    else:								return x == y


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

    print("All done? Earn rewards by using the 'Check' button!")

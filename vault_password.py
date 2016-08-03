# https://github.com/Empire-of-Code-Puzzles/checkio-empire-vault-password

import re
golf=lambda r:re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{10,}",r)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    golf('A1213pokl') == False
    golf('bAse730onE') == True
    golf('asasasasasasasaas') == False
    golf('QWERTYqwerty') == False
    golf('123456123456') == False
    golf('QwErTy911poqqqq') == True
    print("Use 'Check' to earn sweet rewards!")
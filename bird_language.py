# https://github.com/Empire-of-Code-Puzzles/checkio-empire-bird-language

import re
def translate(phrase):
    return ' '.join([''.join([u[0] for u in i]) for i in [re.findall(r'a{3}|e{3}|i{3}|o{3}|u{3}|y{3}|[^aeiouy]', p) for p in phrase.split()]])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

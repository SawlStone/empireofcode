# https://github.com/Empire-of-Code-Puzzles/checkio-empire-three-words

def three_words(words):
    words = words.split(' ')
    for i in range(len(words) - 1):
        if words[i].isalpha() and words[i + 1].isalpha() and words[i + 2].isalpha():
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"

    print("Earn cool rewards by using the 'Check' button!")

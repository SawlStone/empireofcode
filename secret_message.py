# https://github.com/Empire-of-Code-Puzzles/checkio-empire-secret-message

def find_message(text):
    """Find a secret message"""
    return ''.join(i for i in text if i.isupper())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Earn cool rewards by using the 'Check' button!")

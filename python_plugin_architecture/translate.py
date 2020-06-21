import string


def translate(char: str):
    shift = 1
    letters = string.ascii_lowercase
    if char in letters:
        return letters[(letters.index(char) + shift) % len(letters)]
    return char

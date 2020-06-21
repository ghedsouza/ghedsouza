import sys
from translate import translate


def encrypt():
    data = sys.stdin.readlines()
    for line in data:
        for char in line:
            print(translate(char))


encrypt()

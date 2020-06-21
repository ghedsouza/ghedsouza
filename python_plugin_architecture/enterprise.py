import sys
import abc

from translate import translate


class CharReader(abc.ABC):
    @abc.abstractmethod
    def read_char(self):
        pass


class CharWriter(abc.ABC):
    @abc.abstractmethod
    def write_char(self, char: str):
        pass


def encrypter(reader: CharReader, writer: CharWriter):
    def encrypt():
        while True:
            try:
                char = reader.read_char()
            except StopIteration:
                break
            encrypted_char = translate(char)
            writer.write_char(encrypted_char)

    return encrypt


class MyCharReader(CharReader):
    def __init__(self):
        def get_characters():
            data = sys.stdin.readlines()
            for line in data:
                for char in line:
                    yield char

        self.iter = get_characters()

    def read_char(self):
        return next(self.iter)


class MyCharWriter(CharWriter):
    def write_char(self, char: str):
        print(char)


my_encrypter = encrypter(MyCharReader(), MyCharWriter())
my_encrypter()

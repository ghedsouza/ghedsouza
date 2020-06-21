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

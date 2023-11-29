#!/opt/homebrew/bin/python3

from enum import Enum


class Type(Enum):
    FILE = 1
    DIRECTORY = 2
    COMMAND = 3


class FSElement:
    def parent(self):
        pass

    def name(self) -> str:
        pass

    def size(self) -> int:
        pass

    def type(self) -> Type:
        pass


class File(FSElement):
    __name: str
    __size: int
    __parent: FSElement
    __type = Type.FILE

    def __init__(self, string: str, parent: FSElement):
        strElements = string.split(" ")
        self.__name = strElements[1]
        self.__size = strElements[0]
        self.__parent = parent

    def __str__(self):
        return f"{self.__name} (file, size={self.__size})"

    def name(self) -> str:
        return self.__name

    def size(self) -> int:
        return self.__size

    def type(self) -> Type:
        return self.__type

    def parent(self) -> FSElement:
        return self.__parent


class Directory(FSElement):
    __name: str
    __content: []
    __parent: FSElement
    __type = Type.DIRECTORY

    def __init__(self, string, parent: FSElement):
        strElements = string.split(" ")
        self.name = strElements[1]
        self.content = []
        self.__parent = parent

    def __str__(self):
        return f"{self.__name} (dir)"

    def size(self) -> int:
        total = 0
        for element in self.content:
            total += element.size()
        return total

    def add(self, obj):
        self.content.append(obj)



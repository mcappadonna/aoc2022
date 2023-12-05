#!/opt/homebrew/bin/python3

import sys
from enum import Enum


if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <input>")
    exit(1)


class Type(Enum):
    FILE = 1
    DIRECTORY = 2
    COMMAND = 3
    NONE = 4


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

    def __init__(self, string: str, parent: FSElement = None):
        self.__name = string.split(' ')[1]
        self.__content = []
        self.__parent = parent

    def __str__(self):
        output = f"{self.__name} (dir)"
        for element in self.__content:
            output += f"  - \n{element}"
        return output

    def size(self) -> int:
        total = 0
        for element in self.content:
            total += element.size()
        return total

    def add(self, obj):
        self.content.append(obj)

    def content(self):
        return self.__content


def linetype(line: str) -> Type:
    if line[0] == '$':
        return Type.COMMAND
    elif line[0] == 'd':
        return Type.DIRECTORY
    elif line[0].isdigit():
        return Type.FILE
    return Type.NONE


def command(cmdline: str):
    return cmdline.split(' ')[1]


def argument(cmdline: str):
    return cmdline.split(' ')[2]


with open(sys.argv[1], 'r') as f:
    output = f.readlines()
    root = Directory("dir /")
    workingdir = root
    lastcommand = ""
    for line in output:
        lineType = linetype(line)
        print(f"type => {lineType}")
        if lineType == Type.COMMAND:
            lastcommand = line
            print(f"command: {line}")
            cmd = command(line)
            if cmd == 'cd':
                arg = argument(line)
                if arg == '..':
                    workingdir = workingdir.parent()
                elif arg == '/':
                    workingdir = root
                else:
                    for content in workingdir.content():
                        if content.name() == argument:
                            workingdir = content
        elif lineType == Type.DIRECTORY:
            print(f"lastcommand: {lastcommand}")
            if command(lastcommand) == 'ls':
                print(f"-> add dir {line}")
                subdir = Directory(line, workingdir)
                workingdir.add(subdir)
        elif lineType == Type.FILE:
            print(f"lastcommand: {lastcommand}")
            if command(lastcommand) == 'ls':
                print(f"-> add file {line}")
                subfile = File(line, workingdir)
                workingdir.add(subfile)

    print(workingdir)
f.close()

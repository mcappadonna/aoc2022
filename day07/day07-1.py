#!/opt/homebrew/bin/python3

import sys
from enum import Enum


if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <input>")
    exit(1)


class Command(Enum):
    cmd: str
    arg: str

    def __init__(self, cmd, arg):
        self.cmd = cmd
        self.arg = arg

    def __str__(self):
        return f"$ {self.cmd} {self.arg}"

    @staticmethod
    def iscommand(line):
        if line[0] == '$':
            return True
        else:
            return False


class FSelement:
    name: str
    parent: None


class Directory(FSelement):
    content: []

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.content = []

    def __str__(self):
        output = f"- {self.name} (dir)\n"
        for content in self.content:
            output += f"  {content}\n"
        return output

    def add(self, content: FSelement):
        self.content.append(content)

    def getdir(self, name: str):
        subdir = None
        for element in self.content:
            if element.name == name:
                subdir = element
                break
        return subdir

    @staticmethod
    def isdirectory(line: str):
        if line.split(' ')[0].isascii():
            return True
        else:
            return False


class File(FSelement):
    size: int

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"

    @staticmethod
    def isfile(line: str):
        if line.split(' ')[0].isdigit():
            return True
        else:
            return False


def load(file):
    content = file.readlines()
    normalized = []
    for line in content:
        normalized.append(line[:-1])
    return normalized


with open(sys.argv[1], "r") as f:
    content = load(f)

    root = Directory("/")
    cwd = root
    command = None

    for line in content:
        linearray = line.split(' ')
        if Command.iscommand(line):
            command = Command(linearray[1], linearray[2])
            if command.cmd == 'cd':
                if command.arg == '/':
                    cwd = root
                elif command.arg == '..':
                    if cwd != root and cwd.parent:
                        cwd = cwd.parent
                else:
                    subdir = cwd.getdir(command.arg)
                    if subdir is None:
                        cwd = subdir

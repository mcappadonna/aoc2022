#!/opt/homebrew/bin/python3

import sys


if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <input>")
    exit(1)


class Command:
    cmd: str
    arg: str

    def __init__(self, cmd, arg=None):
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


class FSdirectory(FSelement):
    content: []

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.content = []

    def add(self, content: FSelement):
        self.content.append(content)

    def getdir(self, name: str):
        subdir = None
        for element in self.content:
            if element.name == name:
                subdir = element
                break
        return subdir

    def getsubdirs(self) -> []:
        subdirs = []
        for element in self.content:
            if type(element) is FSdirectory:
                subdirs.append(element)
                subdirs += element.subdirs()
        return subdirs

    def getsize(self):
        size = 0
        for elem in self.content:
            size += elem.getsize()
        return size

    @staticmethod
    def isdirectory(line: str):
        if line.split(' ')[0].isascii():
            return True
        else:
            return False


class FSfile(FSelement):
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def getsize(self):
        return self.size

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

    root = FSdirectory("/")
    cwd = root
    command = None

    for line in content:
        linearray = line.split(' ')
        if Command.iscommand(line):
            if len(linearray) == 3:
                command = Command(linearray[1], linearray[2])
            else:
                command = Command(linearray[1])
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
        else:
            if linearray[0] == 'dir':
                newcontent = FSdirectory(linearray[1], cwd)
                cwd.add(newcontent)
            else:
                newcontent = FSfile(linearray[1], int(linearray[0]))
                newcontent.parent = cwd
                cwd.add(newcontent)

    total = 0
    limit = 100000
    for element in root.content:
        if type(element) is FSdirectory:
            dirsize = element.getsize()
            if dirsize <= limit:
                total += dirsize
                for subdir in element.getsubdirs():
                    total += subdir.getsize()
    print(f"{total}")
f.close()

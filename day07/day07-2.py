#!/opt/homebrew/bin/python3

from dataclasses import dataclass

filename = "input"


@dataclass
class FSdirectory():
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.content = []

    def cd(self, name: str):
        output = None
        for element in self.content:
            if element.name == name:
                output = element
                break
        return output

    def add(self, element):
        self.content.append(element)

    def size(self) -> int:
        total: int = 0
        for element in self.content:
            total += element.size()
        return total


@dataclass
class FSfile():
    def __init__(self, name: str, size: int):
        self.name = name
        self.dimension = size

    def size(self) -> int:
        return self.dimension


def load(file):
    content = file.readlines()
    normalized = []
    for line in content:
        normalized.append(line[:-1])
    return normalized


def find(filetype: str, directory):
    results = []
    if filetype != "d" and filetype != "f":
        print(f"Warning: file type {filetype} doesn't recognized")
    else:
        for element in directory.content:
            if filetype == "d" and isinstance(element, FSdirectory):
                results.append(element)
                results = results + find(filetype, element)
            elif filetype == "f" and isinstance(element, FSfile):
                results.append(element)
    return results


with open(filename, "r") as f:
    content = load(f)

    root = FSdirectory("/", None)
    cwd = root

    # Import the filesystem structure
    for line in content:
        linearray = line.split(' ')
        if linearray[0] == "$":
            if linearray[1] == "cd":
                if linearray[2] == "/":
                    cwd = root
                elif linearray[2] == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.cd(linearray[2])
        else:
            if linearray[0] == "dir":
                subdir = FSdirectory(linearray[1], cwd)
                cwd.add(subdir)
            else:
                subfile = FSfile(linearray[1], int(linearray[0]))
                cwd.add(subfile)

    disksize = 70000000
    spaceneeded = 30000000
    unusedspace = disksize - root.size()
    minsize = spaceneeded - unusedspace

    enough = []
    if root.size() >= minsize:
        enough.append(root)
    for directory in find("d", root):
        if directory.size() >= minsize:
            enough.append(directory)

    smallest = disksize
    for directory in enough:
        size = directory.size()
        if size < smallest:
            smallest = size
    print(smallest)
f.close()

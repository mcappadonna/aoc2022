#!/opt/homebrew/bin/python3
from dataclasses import dataclass
from enum import Enum

filename = "input"


class Cardinal(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    NOLINE = 4
    SAME = 5


@dataclass
class Tree():
    def __init__(self, map, x, y):
        self.x = x
        self.y = y
        self.map = map

    def __str__(self):
        return f"{self.height()}"

    def height(self) -> int:
        return int(map[self.y][self.x])

    def is_perimetral(self) -> bool:
        if self.x == 0 or self.x == len(self.map[0])-1 or self.y == 0 or self.y == len(self.map)-1:
            return True
        return False

    def is_visible(self) -> bool:
        return self.visible(Cardinal.NORTH) or self.visible(Cardinal.SOUTH) or self.visible(Cardinal.EAST) or self.visible(Cardinal.WEST)

    def visible(self, watched_from: Cardinal) -> bool:
        if self.is_perimetral():
            return True

        if watched_from == Cardinal.NORTH or watched_from == Cardinal.SOUTH:
            therange = None
            if watched_from == Cardinal.NORTH:
                therange = range(0, self.y)
            else:
                therange = range(self.y+1, len(self.map))

            for y in therange:
                if int(map[y][self.x]) >= self.height():
                    return False
        elif watched_from == Cardinal.WEST or watched_from == Cardinal.EAST:
            therange = None
            if watched_from == Cardinal.WEST:
                therange = range(0, self.x)
            else:
                therange = range(self.x+1, len(self.map[0]))

            for x in therange:
                if int(map[self.y][x]) >= self.height():
                    return False
        return True


def read_and_normalize(file) -> []:
    content = file.readlines()
    for idx in range(0, len(content)):
        content[idx] = content[idx].replace("\n", "")
    return content


def get_tree(map, x, y) -> str:
    return map[y][x]


with open(filename, "r") as f:
    map = read_and_normalize(f)
    visible_count = 0

    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            tree = Tree(map, x, y)
            if tree.is_visible():
                visible_count += 1

    print(f"{visible_count}")
f.close()

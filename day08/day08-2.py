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

    def view_distance(self, to: Cardinal) -> int:
        distance = 0
        if to == Cardinal.NORTH or to == Cardinal.SOUTH:
            start = 0
            end = 0
            step = 0
            if to == Cardinal.NORTH:
                start = self.y-1 if self.y > 0 else 0
                end = -1 if self.y > 0 else 0
                step = -1
            else:
                start = self.y+1 if self.y < len(self.map) else len(self.map)
                end = len(self.map)
                step = 1
            therange = range(start, end, step)
            print(f"- Range {therange}")
            for y in therange:
                distance += 1
                if int(map[y][self.x]) >= self.height():
                    break
        else:
            start = 0
            end = 0
            step = 0
            if to == Cardinal.WEST:
                start = self.x-1 if self.x > 0 else 0
                end = -1 if self.x > 0 else 0
                step = -1
            else:
                start = self.x+1 if self.x < len(self.map[0]) else len(self.map[0])
                end = len(self.map[0])
                step = 1
            therange = range(start, end, step)
            print(f"- Range {therange}")

            for x in therange:
                distance += 1
                if int(map[self.y][x]) >= self.height():
                    break
        return distance

    def scenic_score(self):
        print(f"${self} ({self.x},{self.y})")
        north = self.view_distance(Cardinal.NORTH)
        print(f"- north {north}")
        south = self.view_distance(Cardinal.SOUTH)
        print(f"- south {south}")
        east = self.view_distance(Cardinal.EAST)
        print(f"- east {east}")
        west = self.view_distance(Cardinal.WEST)
        print(f"- west {west}")
        return north * south * east * west


def read_and_normalize(file) -> []:
    content = file.readlines()
    for idx in range(0, len(content)):
        content[idx] = content[idx].replace("\n", "")
    return content


with open(filename, "r") as f:
    map = read_and_normalize(f)
    highest_scenic_score = 0

    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            tree = Tree(map, x, y)
            scenic_score = tree.scenic_score()
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    print(f"{highest_scenic_score}")
f.close()

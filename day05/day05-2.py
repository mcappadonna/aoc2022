#!/opt/homebrew/bin/python3

import sys

if len(sys.argv) != 4:
    print(f"usage: {sys.argv[0]} <input> <mapWidth> <mapHeight>")
    exit(1)

input = sys.argv[1]
mapWidth = int(sys.argv[2])
mapHeight = int(sys.argv[3])


def normalize(lines: []):
    normalized = []
    for line in lines:
        normalized.append(line[:-1])
    return normalized


def columnToIndex(column: int):
    index = 1
    for r in range(1, column):
        index += 4
    return index


def mapToArray(map: [], columns: int, rows: int):
    mapArray = []
    for c in range(0, columns):
        column = []
        index = columnToIndex(c+1)
        for r in range(rows-1, -1, -1):
            if map[r][index] != ' ':
                column.append(map[r][index])
        mapArray.append(column)
    return mapArray


def move(source: [], dest: [], count: int):
    arm = []
    for c in range(0, count):
        crane = source.pop()
        arm.append(crane)
    for e in range(0, len(arm)):
        crane = arm.pop()
        dest.append(crane)


def printTop(mapArray: []):
    for column in mapArray:
        if len(column) == 0:
            print(' ', end='')
        else:
            print(column.pop(), end='')
    print("")


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    map = normalize(lines[0:mapHeight])
    instructions = normalize(lines[mapHeight+2:])

    mapArray = mapToArray(map, mapWidth, mapHeight)

    for inst in instructions:
        splitInst = inst.split(' ')
        iCount = int(splitInst[1])
        iFrom = int(splitInst[3])-1
        iTo = int(splitInst[5])-1
        move(mapArray[iFrom], mapArray[iTo], iCount)

    printTop(mapArray)

f.close()

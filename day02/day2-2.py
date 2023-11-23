#!/opt/homebrew/bin/python3

import sys
from os.path import exists
from enum import Enum

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <file>")
    exit(1)

file = sys.argv[1]
if not exists(file):
    print(f"File {file} doesn't exists")
    exit(1)


class Player(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

    @classmethod
    def from_code(cls, code: str):
        if code == 'A' or code == 'X':
            return cls(Player.Rock)
        elif code == 'B' or code == 'Y':
            return cls(Player.Paper)
        else:
            return cls(Player.Scissor)


class Result(Enum):
    Win = 6
    Lost = 0
    Draw = 3

    @classmethod
    def from_code(cls, code: str):
        if code == 'X':
            return cls(Result.Lost)
        elif code == 'Y':
            return cls(Result.Draw)
        else:
            return cls(Result.Win)


def play(versus: Player, to: Result):
    if to == Result.Win:
        if versus == Player.Rock:
            return Player.Paper
        elif versus == Player.Paper:
            return Player.Scissor
        else:
            return Player.Rock
    elif to == Result.Lost:
        if versus == Player.Rock:
            return Player.Scissor
        elif versus == Player.Paper:
            return Player.Rock
        else:
            return Player.Paper
    else:
        return versus


points = 0

with open(file, "r") as f:
    for line in f.readlines():
        opponent = Player.from_code(line[0])
        result = Result.from_code(line[2])
        player = play(opponent, result)
        points += player.value + result.value

print(points)

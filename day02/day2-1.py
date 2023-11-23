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


def game(opponent: Player, player: Player):
    if opponent == Player.Rock:
        if player == Player.Rock:
            return Result.Draw
        elif player == Player.Paper:
            return Result.Win
        else:
            return Result.Lost
    elif opponent == Player.Paper:
        if player == Player.Rock:
            return Result.Lost
        elif player == Player.Paper:
            return Result.Draw
        else:
            return Result.Win
    else:
        if player == Player.Rock:
            return Result.Win
        elif player == Player.Paper:
            return Result.Lost
        else:
            return Result.Draw


points = 0

with open(file, "r") as f:
    for line in f.readlines():
        opponent = Player.from_code(line[0])
        player = Player.from_code(line[2])
        result = game(opponent, player)
        points += player.value + result.value

print(points)

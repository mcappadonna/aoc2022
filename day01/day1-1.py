#!/opt/homebrew/bin/python3

import sys
from os.path import exists


if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <file>")
    exit(1)

file = sys.argv[1]
if not exists(file):
    print(f"file {file} doesn't exist")
    exit(1)

# Some usefull variables
calories = 0
max_calories = 0
max_calories_elf = 0
elf = 1


# Check if the current elf carries the maximum amount of calories
def bigger_elf(calories):
    if calories > max_calories:
        return True
    return False


with open(file, 'r') as f:
    lines = f.readlines()
    lastline = lines[-1]
    for line in lines:
        if line == '\n' or line == lastline:
            if bigger_elf(calories):
                max_calories = calories
                max_calories_elf = elf
            calories = 0
            elf += 1
            continue

        calories += int(line)
f.close()

print(max_calories_elf, max_calories)

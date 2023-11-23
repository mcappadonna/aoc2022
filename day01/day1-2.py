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
max_calories_elf = [0, 0, 0]
elf = 1


# Check if the current elf carries the maximum amount of calories
def in_top_three(calories):
    podium = False
    for c in max_calories_elf:
        if calories > c:
            podium = True
    return podium


# Add calories to the top three
def add_to_top_three(calories):
    if not in_top_three(calories):
        return
    else:
        switch = 0
        for i in range(len(max_calories_elf)):
            if calories > max_calories_elf[i]:
                switch = max_calories_elf[i]
                max_calories_elf[i] = calories
                break
        add_to_top_three(switch)


# Calculate total calories from the top three
def top_three_calories():
    tot_calories = 0
    for c in max_calories_elf:
        tot_calories += c
    return tot_calories


with open(file, 'r') as f:
    lines = f.readlines()
    lastline = lines[-1]
    for line in lines:
        if line != '\n':
            calories += int(line)
        if line == '\n' or line == lastline:
            add_to_top_three(calories)
            calories = 0
            elf += 1
            continue

f.close()

print(top_three_calories())

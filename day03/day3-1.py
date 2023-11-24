#!/opt/homebrew/bin/python3

def find_match(comp1: str, comp2: str):
    match = ''
    for letter1 in comp1:
        for letter2 in comp2:
            if letter1 == letter2:
                match = letter1
                break
    return match


# Match: a (97)
# Match: A (65)
# a..z = 1..26
# A..Z = 27..52
lowercase_delta = 96
uppercase_delta = 38


def match_to_number(match, delta):
    return ord(match)-delta


def get_delta(match: str):
    if match.islower():
        return lowercase_delta
    else:
        return uppercase_delta


priorities = 0
with open('input', 'r') as f:
    for rucksack in f.readlines():
        half = int(len(rucksack) / 2)
        first_compartment = rucksack[0:half]
        second_compartment = rucksack[half:]
        match = find_match(first_compartment, second_compartment)
        delta = get_delta(match)
        priorities += match_to_number(match, delta)

print(priorities)

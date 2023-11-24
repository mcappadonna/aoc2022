#!/opt/homebrew/bin/python3

def update_items(elf: str, items: {}):
    for item in elf:
        if item not in items:
            items.update({item: 1})
        else:
            items[item] += 1
    return items


def uniq(string: str):
    uniq = ""
    for char in string:
        if char not in uniq:
            uniq += char
    return uniq


def find_match(elves: []):
    items = {}
    match = ""
    for elf in elves:
        items = update_items(elf, items)
    for key in items.keys():
        if items[key] == 3:
            match = key
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
    index = 0
    group_size = 3
    elves = ["", "", ""]
    for rucksack in f.readlines():
        elves[index] = uniq(rucksack[:-1])
        index += 1
        if index == group_size:
            match = find_match(elves)
            priorities += match_to_number(match, get_delta(match))
            index = 0
f.close()

print(priorities)

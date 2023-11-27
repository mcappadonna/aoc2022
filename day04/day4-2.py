#!/opt/homebrew/bin/python3

def overlap(elf1: range, elf2: range):
    for section1 in elf1:
        for section2 in elf2:
            if section1 == section2:
                return True
    return False


with open('input', 'r') as f:
    fullyContains = 0
    elves = []
    for pair in f.readlines():
        for pairString in pair.replace('\n', '').split(','):
            pairNumbers = pairString.split('-')
            pairRange = range(int(pairNumbers[0]), int(pairNumbers[1])+1)
            elves.append(pairRange)
        if overlap(elves[0], elves[1]):
            fullyContains += 1
        elves = []
    print(fullyContains)
f.close()

#!/opt/homebrew/bin/python3

def checkContains(elf1: range, elf2: range):
    if elf1.start >= elf2.start and elf1.stop <= elf2.stop:
        return True
    elif elf2.start >= elf1.start and elf2.stop <= elf1.stop:
        return True
    return False


with open('input', 'r') as f:
    fullyContains = 0
    elves = []
    for pair in f.readlines():
        for pairString in pair.replace('\n', '').split(','):
            pairNumbers = pairString.split('-')
            pairRange = range(int(pairNumbers[0]), int(pairNumbers[1]))
            elves.append(pairRange)
        if checkContains(elves[0], elves[1]):
            fullyContains += 1
        elves = []
    print(fullyContains)
f.close()

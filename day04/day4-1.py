#!/opt/homebrew/bin/python3

with open('input', 'r') as f:
    for pair in f.readlines():
        elves = pair.split(',')
        print(elves)
f.close()

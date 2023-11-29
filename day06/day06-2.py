#!/opt/homebrew/bin/python3

import sys

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <input>")
    exit(0)


def isuniq(string: []):
    charMatch = False
    for source in range(0, len(string)):
        for dest in range(0, len(string)):
            if source == dest:
                continue
            if string[source] == string[dest]:
                charMatch = True
                break
    return not charMatch


with open(sys.argv[1], 'r') as f:
    signal = f.readline()

    markerSize = 14
    for idx in range(0, len(signal)):
        markerStart = idx+markerSize
        marker = signal[idx:markerStart]
        if isuniq(marker):
            print(markerStart)
            break
f.close()

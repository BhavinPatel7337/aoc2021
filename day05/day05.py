from sys import path
import re

with open(path[0] + '/input.txt') as f:
    lines = [[int(j) for j in re.split(' -> |,', i)] for i in f.read().splitlines()]

def findOverlaps(includeDiagonals):
    vents = {}
    for x1, y1, x2, y2 in lines:
        new = []
        if x1 == x2:
            new = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
        elif y1 == y2:
            new = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
        elif includeDiagonals:
            if x1 > x2 and y1 > y2:
                new = list(zip(range(x1, x2 - 1, -1), range(y1, y2 - 1, -1)))
            elif x1 > x2 and y2 > y1:
                new = list(zip(range(x1, x2 - 1, -1), range(y1, y2 + 1)))
            elif x2 > x1 and y1 > y2:
                new = list(zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)))
            elif x2 > x1 and y2 > y1:
                new = list(zip(range(x1, x2 + 1), range(y1, y2 + 1)))
        for i in new:
            vents[i] = vents.get(i, 0) + 1
    return len([i for i in vents if vents[i] > 1])

print('Part 1:', findOverlaps(False))
print('Part 2:', findOverlaps(True))
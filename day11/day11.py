from sys import path
from collections import deque

with open(path[0] + '/input.txt') as f:
    octopuses = {(x, y): int(energy) for y, line in enumerate(f.read().splitlines()) for x, energy in enumerate(line)}

def getAdjacent(x, y):
    return set(octopuses) & {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}

flashes = 0
step = 1
while True:
    toIncrement = deque(octopuses)
    flashing = set()
    while (toIncrement):
        current = toIncrement.popleft()
        if current not in flashing:
            octopuses[current] += 1
            if octopuses[current] > 9:
                flashing.add(current)
                toIncrement.extend(getAdjacent(current[0], current[1]))
    for i in flashing:
        octopuses[i] = 0
        flashes += 1
    if step == 100:
        print('Part 1:', flashes)
    if all(e == 0 for e in octopuses.values()):
        print('Part 2:', step)
        break
    step += 1
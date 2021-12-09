from sys import path
from math import prod

with open(path[0] + '/input.txt') as f:
    heightmap = {(x, y): int(height) for y, line in enumerate(f.read().splitlines()) for x, height in enumerate(line)}

def isLowPoint(x, y, height):
    return height < heightmap.get((x - 1, y), 10) and height < heightmap.get((x + 1, y), 10) and height < heightmap.get((x, y - 1), 10) and height < heightmap.get((x, y + 1), 10)

part1 = 0
low_points = set()
for (x, y), height in heightmap.items():
    if isLowPoint(x, y, height):
        low_points.add((x, y))
        part1 += heightmap[x, y] + 1

print('Part 1:', part1)

def getBasin(x, y, basin):
    if (x, y) not in basin:
        basin.add((x, y))
        if heightmap.get((x - 1, y), 9) != 9:
            basin = getBasin(x - 1, y, basin)
        if heightmap.get((x + 1, y), 9) != 9:
            basin = getBasin(x + 1, y, basin)
        if heightmap.get((x, y - 1), 9) != 9:
            basin = getBasin(x, y - 1, basin)
        if heightmap.get((x, y + 1), 9) != 9:
            basin = getBasin(x, y + 1, basin)
    return basin

print('Part 2:', prod(sorted([len(getBasin(x, y, set())) for x, y in low_points])[-3:]))
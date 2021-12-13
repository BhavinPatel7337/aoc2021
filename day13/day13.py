from sys import path
import re
from collections import deque

points = {}
folds = deque()
dim_x, dim_y = 0, 0
with open(path[0] + '/input.txt') as f:
    line = f.readline()
    while line != '\n':
        points[tuple([int(p) for p in line.split(',')])] = '#'
        line = f.readline()
    line = f.readline()
    while line and line != '\n':
        m = re.search('fold along (x|y)=(\d+)', line).groups()
        if m[0] == 'x':
            dim_x = int(m[1])
        elif m[0] == 'y':
            dim_y = int(m[1])
        folds.append((m[0], int(m[1])))
        line = f.readline()

def foldPaper(fold):
    for p in points.copy():
        if fold[0] == 'x':
            if p[0] > fold[1]:
                points[(fold[1] - (p[0] - fold[1]), p[1])] = '#'
                points.pop(p)
        elif fold[0] == 'y':
            if p[1] > fold[1]:
                points[(p[0], fold[1] - (p[1] - fold[1]))] = '#'
                points.pop(p)

foldPaper(folds.popleft())
print('Part 1:', len(points))
print('Part 2:')
while folds:
    foldPaper(folds.popleft())
for y in range(dim_y):
    line = ''
    for x in range(dim_x):
        line += points.get((x, y), ' ')
    print(line)

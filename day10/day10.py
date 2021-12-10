from sys import path
from collections import deque

with open(path[0] + '/input.txt') as f:
    lines = [x for x in f.read().splitlines()]

opposite = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_table = {'(': 1, '[': 2, '{': 3, '<': 4}
part1 = 0
part2 = []
for line in lines:
    stack = deque()
    valid = True
    for i in line:
        if i in ['(', '[', '{', '<']:
            stack.append(i)
        elif i in [')', ']', '}', '>']:
            if not opposite[stack.pop()] == i:
                part1 += error_table[i]
                valid = False
                break
    if valid:
        score = 0
        while stack:
            score = score * 5 + completion_table[stack.pop()]
        part2.append(score)
print('Part 1:', part1)
print('Part 2:', sorted(part2)[int(len(part2) / 2)])
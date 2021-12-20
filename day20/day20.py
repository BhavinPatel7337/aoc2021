from sys import path
from collections import defaultdict
from functools import reduce
from itertools import product

with open(path[0] + '/input.txt') as f:
    alg, inp = f.read().split('\n\n')

alg = [x == '#' for x in alg.replace('\n', '')]
img = defaultdict(lambda: False)
for y, line in enumerate(inp.splitlines()):
    for x, px in enumerate(line):
        img[x, y] = px == '#'

def get_index(x, y):
    return reduce(lambda a, b: (a << 1) + int(b), [img[x + dx, y + dy] for dy, dx in product(range(-1, 2), repeat=2)])

def enhance(min_x, min_y, max_x, max_y, i):
    new_img = defaultdict(lambda: alg[0] and not i % 2)
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            new_img[x, y] = alg[get_index(x, y)]
    return new_img

for i in range(50):
    img = enhance(-i, -i, x + i, y + i, i)
    if i == 1:
        print('Part 1:', sum(img.values()))
    elif i == 49:
        print('Part 2:', sum(img.values()))
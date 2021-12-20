from sys import path
from collections import defaultdict

with open(path[0] + '/input.txt') as f:
    alg, inp = f.read().split('\n\n')

alg = [x == '#' for x in alg.replace('\n', '')]
x, y, i = 0, 0, 0
img = defaultdict(lambda: False)
while i < len(inp.rstrip()):
    if inp[i] == '#':
        img[x, y] = True
    elif inp[i] == '\n':
        x = -1
        y += 1
    x += 1
    i += 1

min_x, min_y, max_x, max_y = 0, 0, x - 1, y

def get_index(x, y):
    return int(''.join(str(int(img[c])) for c in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]), 2)

def enhance(min_x, min_y, max_x, max_y, i):
    new_img = defaultdict(lambda: alg[0] and i % 2 == 0)
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            new_img[x, y] = alg[get_index(x, y)]
    return new_img

for i in range(50):
    img = enhance(min_x, min_y, max_x, max_y, i)
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    if i == 1:
        print('Part 1:', sum(img.values()))
    elif i == 49:
        print('Part 2:', sum(img.values()))
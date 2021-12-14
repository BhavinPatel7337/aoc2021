from sys import path
from collections import Counter
from collections import defaultdict
import math

with open(path[0] + '/input.txt') as f:
    template = f.readline().strip()
    f.readline()
    rules = {y[0]: y[1] for x in f.read().splitlines() if (y := x.split(' -> '))}

pair_count = defaultdict(int)
for i in range(len(template) - 1):
    pair_count[template[i] + template[i + 1]] += 1

def polymerise():
    for p, c in pair_count.copy().items():
        pair_count[p] -= c
        pair_count[p[0] + rules[p]] += c
        pair_count[rules[p] + p[1]] += c

def get_answer():
    polymer_counts = defaultdict(int)
    for p, c in pair_count.items():
        for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if p == x + x:
                polymer_counts[x] += c
            elif x in p:
                polymer_counts[x] += c / 2
    return math.ceil(max(polymer_counts.values())) - math.ceil(min(polymer_counts.values()))

for _ in range(10):
    polymerise()
print('Part 1:', get_answer())

for _ in range(30):
    polymerise()
print('Part 2:', get_answer())
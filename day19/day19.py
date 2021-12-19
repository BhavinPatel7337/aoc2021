from sys import path
import re
from itertools import combinations, permutations
from collections import defaultdict

class Scanner:
    def __init__(self, name):
        self.name = name
        self.pos = (0, 0, 0)
        self.orient = []
        self.beacons = defaultdict(lambda: [])

    def add_beacons(self, beacons):
        for b1, b2 in permutations(beacons, 2):
            self.beacons[b1].append((b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2]))

def transform(x, y, z, i):
    t = {
        0: (x, y, z), 1: (x, z, -y), 2: (x, -y, -z), 3: (x, -z, y),
        4: (y, -z, -x), 5: (y, -x, z), 6: (y, z, x), 7: (y, x, -z),
        8: (z, x, y), 9: (z, -y, x), 10: (z, -x, -y), 11: (z, y, -x),
        12: (-x, y, -z), 13: (-x, z, y), 14: (-x, -y, z), 15: (-x, -z, -y),
        16: (-y, z, -x), 17: (-y, x, z), 18: (-y, -z, x), 19: (-y, -x, -z),
        20: (-z, -x, y), 21: (-z, -y, -x), 22: (-z, x, -y), 23: (-z, y, x)
    }
    return t[i]

def get_abs_pos(ref_pos, ref_orient, rel_pos):
    for o in ref_orient:
        rel_pos = transform(*rel_pos, o)
    return tuple(sum(x) for x in zip(ref_pos, rel_pos))

def find_scanner_pos(sc1, sc2):
    for i in range(23):
        shared = []
        for b2, v2 in sc2.beacons.items():
            v2_t = [transform(*d, i) for d in v2]
            for b1, v1 in sc1.beacons.items():
                a = set(v1) & set(v2_t)
                if len(a) > 10:
                    shared.append((b1, b2))
        if len(shared) > 11:
            sc2.orient = [i] + sc1.orient
            b1, b2 = shared[0]
            b2 = transform(*b2, i)
            rel_pos = (b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2])
            sc2.pos = get_abs_pos(sc1.pos, sc1.orient, rel_pos)
            for b in sc2.beacons:
                known_beacons.add(get_abs_pos(sc2.pos, sc2.orient, b))
            return sc2
    return None

unknown_scanners = []
with open(path[0] + '/input.txt') as f:
    while (line := f.readline()):
        m = re.search('\-\-\- scanner (\d+) \-\-\-', line)
        if m:
            sc = Scanner(m.group(1))
            b = set()
        elif line != '\n':
            b.add(tuple([int(x) for x in line.strip().split(',')]))
        else:
            sc.add_beacons(b)
            unknown_scanners.append(sc)
    sc.add_beacons(b)
    unknown_scanners.append(sc)

sc1 = unknown_scanners.pop(0)
known_scanners = [sc1]
known_beacons = set(sc1.beacons.keys())
i = 0
while unknown_scanners:
    sc1 = known_scanners[i]
    for sc2 in unknown_scanners.copy():
        if find_scanner_pos(sc1, sc2):
            known_scanners.append(sc2)
            unknown_scanners.remove(sc2)
    i += 1

print('Part 1:', len(known_beacons))

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

print('Part 2:', max(manhattan_distance(sc1.pos, sc2.pos) for sc1, sc2 in combinations(known_scanners, 2)))
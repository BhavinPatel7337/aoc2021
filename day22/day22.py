from sys import path
import re

with open(path[0] + '/input.txt') as f:
    cuboids = [re.search('(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', line).groups() for line in f.read().splitlines()]
    cuboids = [(state == 'on', int(min_x), int(max_x), int(min_y), int(max_y), int(min_z), int(max_z)) for state, min_x, max_x, min_y, max_y, min_z, max_z in cuboids]

def volume(c):
    return (abs(c[2] - c[1]) + 1) * (abs(c[4] - c[3]) + 1) * (abs(c[6] - c[5]) + 1)

def get_overlap(a, b):
    return b[0], max(a[1], b[1]), min(a[2], b[2]), max(a[3], b[3]), min(a[4], b[4]), max(a[5], b[5]), min(a[6], b[6])

def check_overlap(a, b):
    return a[1] <= b[2] and a[2] >= b[1] and a[3] <= b[4] and a[4] >= b[3] and a[5] <= b[6] and a[6] >= b[5]

def slice_cube(a, b):
    slices = []
    if a[1] < b[1]: # left
        slices.append((True, a[1], b[1] - 1, a[3], a[4], a[5], a[6]))
    if a[2] > b[2]: # right
        slices.append((True, b[2] + 1, a[2], a[3], a[4], a[5], a[6]))
    if a[3] < b[3]: # bottom
        slices.append((True, b[1], b[2], a[3], b[3] - 1, a[5], a[6]))
    if a[4] > b[4]: # top
        slices.append((True, b[1], b[2], b[4] + 1, a[4], a[5], a[6]))
    if a[5] < b[5]: # front
        slices.append((True, b[1], b[2], b[3], b[4], a[5], b[5] - 1))
    if a[6] > b[6]: # back
        slices.append((True, b[1], b[2], b[3], b[4], b[6] + 1, a[6]))
    return slices

def reboot(init):
    lit = []
    for new_cube in cuboids:
        if init:
            state, min_x, max_x, min_y, max_y, min_z, max_z = new_cube
            if min_x > 50 or max_x < -50 or min_y > 50 or max_y < -50 or min_z > 50 or max_z < -50:
                continue
            new_cube = (state, max(min_x, -50), min(max_x, 50), max(min_y, -50), min(max_y, 50), max(min_z, -50), min(max_z, 50))
        for c in lit.copy():
            if check_overlap(new_cube, c):
                overlap = get_overlap(c, new_cube)
                slices = slice_cube(c, overlap)
                lit.remove(c)
                lit += slices
        if new_cube[0]:
            lit.append(new_cube)
    return sum(volume(c) for c in lit)

print('Part 1:', reboot(True))
print('Part 2:', reboot(False))
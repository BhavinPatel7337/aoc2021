from sys import path
import re

with open(path[0] + '/input.txt') as f: 
    min_x, max_x, min_y, max_y = [int(x) for x in re.search('x=(\-?\d+)\.\.(\-?\d+), y=(\-?\d+)\.\.(\-?\d+)', f.read()).groups()]

def step(pos_x, pos_y, vel_x, vel_y):
    new_pos_x = pos_x + vel_x
    new_pos_y = pos_y + vel_y
    if vel_x > 0:
        new_vel_x = vel_x - 1
    elif vel_x < 0:
        new_vel_x = vel_x + 1
    else:
        new_vel_x = vel_x
    new_vel_y = vel_y - 1
    return (new_pos_x, new_pos_y, new_vel_x, new_vel_y)

def testVelocity(vel_x, vel_y):
    pos_x, pos_y, highest = 0, 0, 0
    while pos_x <= max_x and pos_y >= min_y:
        if pos_y > highest:
            highest = pos_y
        if pos_x >= min_x and pos_y <= max_y:
            return True, highest
        pos_x, pos_y, vel_x, vel_y = step(pos_x, pos_y, vel_x, vel_y)
    return False, highest

part1 = 0
part2 = 0
test = 0
for vel_x in range(0, max_x + 1):
    for vel_y in range(-abs(min_y), abs(min_y)):
        in_target, highest = testVelocity(vel_x, vel_y)
        if in_target:
            if highest > part1:
                part1 = highest
            part2 += 1
            if vel_y > test:
                test = vel_y            

print('Part 1:', part1)
print('Part 2:', part2)
from sys import path

with open(path[0] + '/input.txt') as f:
    course = f.read().splitlines()

pos, depth1, depth2, aim = 0, 0, 0, 0
for command in course:
    direction, value = command.split(' ')
    if direction == 'forward':
        pos += int(value)
        depth2 += aim * int(value)
    elif direction == 'up':
        depth1 -= int(value)
        aim -= int(value)
    elif direction == 'down':
        depth1 += int(value)
        aim += int(value)

print("Part 1:", pos * depth1)
print("Part 2:", pos * depth2)
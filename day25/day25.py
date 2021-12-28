from sys import path

with open(path[0] + '/input.txt') as f:
    seafloor_map = {(x, y): space for y, line in enumerate(f.read().splitlines()) for x, space in enumerate(line)}

dimensions = max(seafloor_map)

def move_east(sf_map, dimensions):
    new_map = sf_map.copy()
    movable = []
    for y in range(dimensions[1] + 1):
        for x in range(dimensions[0] + 1):
            if sf_map[x, y] == '>' and sf_map[(x + 1) % (dimensions[0] + 1), y] == '.':
                    movable.append((x, y))
    for x, y in movable:
        new_map[x, y] = '.'
        new_map[(x + 1) % (dimensions[0] + 1), y] = '>'
    return new_map

def move_south(sf_map, dimensions):
    new_map = sf_map.copy()
    movable = []
    for y in range(dimensions[1] + 1):
        for x in range(dimensions[0] + 1):
            if sf_map[x, y] == 'v' and sf_map[x, (y + 1) % (dimensions[1] + 1)] == '.':
                    movable.append((x, y))
    for x, y in movable:
        new_map[x, y] = '.'
        new_map[x, (y + 1) % (dimensions[1] + 1)] = 'v'
    return new_map

i = 1
while True:
    new_map = move_east(seafloor_map, dimensions)
    new_map = move_south(new_map, dimensions)
    if seafloor_map == new_map:
        break
    else:
        seafloor_map = new_map
        i += 1

print('Part 1:', i)
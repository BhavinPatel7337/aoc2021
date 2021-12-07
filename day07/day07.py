from sys import path

with open(path[0] + '/input.txt') as f:
    crabs = [int(x) for x in f.read().split(',')]

min_fuel1 = (0, sum(crabs))
min_fuel2 = (0, sum([x * (x + 1) / 2 for x in crabs]))
for i in range(1, max(crabs)):
    fuel1 = sum([abs(x - i) for x in crabs])
    fuel2 = int(sum([abs(x - i) * (abs(x - i) + 1) / 2 for x in crabs]))
    if fuel1 < min_fuel1[1]:
        min_fuel1 = (i, fuel1)
    if fuel2 < min_fuel2[1]:
        min_fuel2 = (i, fuel2)

print('Part 1:', min_fuel1[1])
print('Part 2:', min_fuel2[1])
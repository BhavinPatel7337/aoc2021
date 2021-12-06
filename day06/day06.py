from sys import path

with open(path[0] + '/input.txt') as f:
    fish = [int(x) for x in f.read().split(',')]

def simulate(fish, days):
    counts = [fish.count(i) for i in range(9)]
    for i in range(days):
        counts = counts[1:] + [counts[0]]
        counts[6] += counts[8]
    return(sum(counts))

print('Part 1:', simulate(fish, 80))
print('Part 2:', simulate(fish, 256))
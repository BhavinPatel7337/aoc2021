from sys import path

with open(path[0] + '/input.txt') as f:
    sonar = [int(x) for x in f]

readings = sonar[0:3]
answer1 = (readings[1] > readings[0]) + (readings[2] > readings[1])
answer2 = 0
for i in range(3, len(sonar)):
    answer1 += sonar[i] > sonar[i - 1]
    answer2 += sonar[i] > readings[i % 3]
    readings[i % 3] = sonar[i]

print("Part 1:", answer1)
print("Part 2:", answer2)
from sys import path
from queue import PriorityQueue
from collections import defaultdict
import math

with open(path[0] + '/input.txt') as f:
    risk_map_1 = {(x, y): int(risk) for y, line in enumerate(f.read().splitlines()) for x, risk in enumerate(line)}

def findPathRisk(risk_map, max_x, max_y):
    shortest_path_found = set()
    cost = defaultdict(lambda: math.inf)
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    while not pq.empty():
        risk, (x, y) = pq.get()
        if (x, y) not in shortest_path_found:
            shortest_path_found.add((x, y))
            new_coords = []
            if x > 0:
                new_coords.append((x - 1, y))
            if x < max_x:
                new_coords.append((x + 1, y))
            if y > 0:
                new_coords.append((x, y - 1))
            if y < max_y:
                new_coords.append((x, y + 1))
            for c in new_coords:
                new_cost = risk + risk_map[c]
                if c not in shortest_path_found and cost[c] > new_cost:
                    cost[c] = new_cost
                    pq.put((new_cost, c))
    return cost[max_x, max_y]

max_x = max(coord[0] for coord in risk_map_1)
max_y = max(coord[1] for coord in risk_map_1)
print('Part 1:', findPathRisk(risk_map_1, max_x, max_y))

risk_map_2 = risk_map_1.copy()
for j in range(5):
    for i in range(5):
        for (x, y), r in risk_map_1.items():
            new_r = r + i + j
            if new_r > 9:
                new_r = new_r % 10 + 1                
            risk_map_2[x + (i * (max_x + 1)), y + (j * (max_y + 1))] = new_r
print('Part 2:', findPathRisk(risk_map_2, ((max_x + 1) * 5) - 1, ((max_y + 1) * 5) - 1))
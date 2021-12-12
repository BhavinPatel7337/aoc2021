from sys import path

cave_map = {}
with open(path[0] + '/input.txt') as f:
    for x in f.read().splitlines():
        route = x.split('-')
        cave_map[route[0]] = cave_map.get(route[0], set()) | {route[1]}
        cave_map[route[1]] = cave_map.get(route[1], set()) | {route[0]}

paths_found = set()
currentPath = []
def findPaths(current, visit_twice):
    if current.islower() and current in currentPath and not (current == visit_twice and currentPath.count(current) < 2):
        return
    if current == 'end':
        paths_found.add(','.join(currentPath.copy()))
        return
    currentPath.append(current)
    for cave in cave_map[current]:
        findPaths(cave, visit_twice)
    currentPath.pop()

findPaths('start', '')
print('Part 1:', len(paths_found))
for cave in cave_map:
    if cave.islower() and cave not in ['start', 'end']:
        findPaths('start', cave)
print('Part 2:', len(paths_found))
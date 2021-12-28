from collections import deque
from copy import deepcopy
import math
from sys import path

class BurrowState:
    def __init__(self, h, l, e, a, b, c, d) -> None:
        self.hallway = h
        self.room_length = l
        self.energy = e
        self.roomA = deque(a)
        self.roomB = deque(b)
        self.roomC = deque(c)
        self.roomD = deque(d)
        self.home = {'A': self.roomA, 'B': self.roomB, 'C': self.roomC, 'D': self.roomD}
        self.door = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    
    def dist_to_door(self, room):
        return self.room_length - len(self.home[room])
    
    def solved(self):
        return all(self.room_valid(x) and x not in self.hallway for x in ['A', 'B', 'C', 'D'])

    def space_reachable(self, start, end, inHallway):
        distance = abs(start - end)
        if inHallway:
            if start < end:
                start += 1
            elif start > end:
                start -= 1
        if all(self.hallway[x] == '.' for x in range(min(start, end), max(start, end) + 1)):
            return distance
        return 0

    def room_valid(self, room_name):
        return all(x == room_name for x in self.home[room_name])
    
def energy_cost(amphipod, distance):
    e = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    return e[amphipod] * distance

def find_moves(state, move_list, min_total_energy):
    # For each space in the hallway
    for i, occupant in enumerate(state.hallway):
        # Check if it contains an amphipod
        if occupant != '.':
            # If the amphipod's room is accessible, move it
            if state.room_valid(occupant):
                if distance := state.space_reachable(i, state.door[occupant], True):
                    new_state = deepcopy(state)
                    new_state.hallway = new_state.hallway[:i] + '.' + new_state.hallway[i + 1:]
                    new_state.home[occupant].appendleft(occupant)
                    new_state.energy += energy_cost(occupant, distance + state.dist_to_door(occupant))
                    if min_total_energy > new_state.energy:
                        move_list.append(new_state)
                    return
    # For each room A-D
    for current_room in state.home:
        # Check if any occupants require moving from this room
        if not state.room_valid(current_room):
            new_state = deepcopy(state)
            first = new_state.home[current_room].popleft()
            # If first occupant's room is valid and reachable, move them into it
            if state.room_valid(first) and (distance := state.space_reachable(state.door[current_room], state.door[first], False)):
                    new_state.home[first].appendleft(first)
                    new_state.energy += energy_cost(first, distance + 1 + state.dist_to_door(current_room) + state.dist_to_door(first))
                    if min_total_energy > new_state.energy:
                        move_list.append(new_state)
                    return
            else:
                # Otherwise generate a new state for the first occupant staying in every accessible hallway space
                for i in [0, 1, 3, 5, 7, 9, 10]:
                    if distance := state.space_reachable(state.door[current_room], i, False):
                        new_state.hallway = new_state.hallway[:i] + first + new_state.hallway[i + 1:]                        
                        new_state.energy += energy_cost(first, distance + state.dist_to_door(current_room) + 1)
                        if min_total_energy > new_state.energy:
                            move_list.append(new_state)
                        new_state = deepcopy(state)
                        first = new_state.home[current_room].popleft()

def solve(initial):
    move_list = deque()
    count = 0
    min_total_energy = math.inf
    move_list.append(initial)
    while move_list:
        current = move_list.pop()
        if min_total_energy > current.energy:
            if current.solved():
                print('New solution found:', current.energy, count)
                min_total_energy = current.energy
            count += 1
            find_moves(current, move_list, min_total_energy)
    print(count)
    return min_total_energy

with open(path[0] + '/input.txt') as f:
    inp = f.read()
    state1 = BurrowState('.' * 11, 2, 0, [inp[31], inp[45]], [inp[33], inp[47]], [inp[35], inp[49]], [inp[37], inp[51]])

print('Part 1:', solve(state1))
a = deque([state1.roomA[0], 'D', 'D', state1.roomA[1]])
b = deque([state1.roomB[0], 'C', 'B', state1.roomB[1]])
c = deque([state1.roomC[0], 'B', 'A', state1.roomC[1]])
d = deque([state1.roomD[0], 'A', 'C', state1.roomD[1]])
state2 = BurrowState('.' * 11, 4, 0, a, b, c, d)
print('Part 2:', solve(state2))
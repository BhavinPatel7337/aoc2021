from sys import path
from itertools import product

with open(path[0] + '/input.txt') as f:
    starting_pos = [int(x.split()[-1]) for x in f.read().splitlines()]

def deterministic_dice(pos):
    total_score = [0, 0]
    current_player = False
    i = 1
    while max(total_score) < 1000:
        die_sum = (((i - 1) % 100) + 1) + (((i) % 100) + 1) + (((i + 1) % 100) + 1)
        round_score = ((pos[int(current_player)] + die_sum - 1) % 10) + 1
        pos[int(current_player)] = round_score
        total_score[int(current_player)] += round_score
        current_player = not current_player
        i += 3
    return min(total_score) * (i - 1)

print('Part 1:', deterministic_dice(starting_pos.copy()))

possibilities = list(product(range(1, 4), repeat=3))
cache = {}
def dirac_dice(pos1, pos2, total_score1, total_score2, current_player):
    state = (pos1, pos2, total_score1, total_score2, current_player)
    wins = [0, 0]
    if state in cache:
        return cache[state]
    if total_score1 >= 21:
        cache[state] = (1, 0)
        return (1, 0)
    elif total_score2 >= 21:
        cache[state] = (0, 1)
        return (0, 1)
    else:
        for p in possibilities:
            if current_player:
                round_score = ((pos2 + sum(p) - 1) % 10) + 1
                new_score = total_score2 + round_score
                next_player = not current_player
                wins1, wins2 = dirac_dice(pos1, round_score, total_score1, new_score, next_player)
            else:
                round_score = ((pos1 + sum(p) - 1) % 10) + 1
                new_score = total_score1 + round_score
                next_player = not current_player
                wins1, wins2 = dirac_dice(round_score, pos2, new_score, total_score2, next_player)
            wins[0] += wins1
            wins[1] += wins2
        cache[state] = (wins[0], wins[1])
        return (wins[0], wins[1])

print('Part 2:', max(dirac_dice(*starting_pos, 0, 0, False)))
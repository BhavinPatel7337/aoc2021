from sys import path

with open(path[0] + '/input.txt') as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]
    boards = []
    board = []
    for line in f:
        if line == '\n' and board:
            boards += [board]
            board = []
        else:
            board += [int(x) for x in line.split()]
    if board:
        boards += [board]

winning_combos = {}
for i, b in enumerate(boards):
    winning_combos[i] = [set(x) for x in [b[0:5], b[5:10], b[10:15], b[15:20], b[20:25], b[::5], b[1::5], b[2::5], b[3::5], b[4::5]]]

def checkWinners(called, winning_boards):
    for b in set(winning_combos) - set(winning_boards):
        for combo in winning_combos[b]:
            if combo.issubset(set(called)):
                winning_boards[b] = sum(set(boards[b]) - set(called)) * called[-1]
                if len(winning_boards) == 1:
                    print('Part 1:', winning_boards[b])
                elif len(winning_boards) == len(winning_combos):
                    print('Part 2:', winning_boards[b])
                    return


i = -1
winning_boards = {}
while len(winning_boards) < len(winning_combos):
    i += 1
    checkWinners(numbers[:i + 1], winning_boards)
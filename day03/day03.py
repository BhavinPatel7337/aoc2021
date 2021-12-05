from sys import path

with open(path[0] + '/input.txt') as f:
    diagnostic = f.read().splitlines()

def get_bit_criteria(lst, mode='o2'):
    counts = {'0': 0, '1': 0}
    for x in lst:
        counts[x] += 1
    if (mode == 'o2' and counts['0'] > counts['1']) or (mode == 'co2' and counts['0'] <= counts['1']):
        return '0'
    else:
        return '1'

gamma = ''
for i in range(len(diagnostic[0])):
    gamma += get_bit_criteria([d[i] for d in diagnostic])
epsilon = gamma.translate(str.maketrans('01', '10'))
print('Part 1:', int(gamma, 2) * int(epsilon, 2))

def get_rating(mode):
    valid = [d for d in diagnostic]
    i = 0
    while len(valid) > 1:
        bit_criteria = get_bit_criteria([v[i] for v in valid], mode)
        valid = [v for v in valid if v[i] == bit_criteria]
        i += 1
    return int(valid[0], 2)

print('Part 2:', get_rating('o2') * get_rating('co2'))
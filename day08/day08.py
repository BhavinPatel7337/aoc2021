from sys import path

with open(path[0] + '/input.txt') as f:
    notes = []
    for x in f.read().splitlines():
        signals, output = x.split(' | ')
        signals = signals.split()
        output = output.split()
        notes.append((signals, output))

part1 = 0
part2 = 0
for signals, output in notes:
    digits = {}
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0}
    for s in signals:
        for chr in s:
            counts[chr] += 1
        if len(s) == 2:
            digits[1] = set(s)
        elif len(s) == 3:
            digits[7] = set(s)
        elif len(s) == 4:
            digits[4] = set(s)
        elif len(s) == 7:
            digits[8] = set(s)
    segment_top = (digits[7] - digits[1]).pop()
    for c, n in counts.items():
        if n == 4:
            segment_bl = c
        elif n == 6:
            segment_ul = c
        elif n == 7:
            if c in digits[4]:
                segment_mid = c
            else:
                segment_bot = c
        elif n == 8 and c != segment_top:
            segment_ur = c
        elif n == 9:
            segment_br = c
    for s in signals:
        if set(s) == {segment_top, segment_ul, segment_ur, segment_bl, segment_br, segment_bot}:
            digits[0] = set(s)
        elif set(s) == {segment_top, segment_ur, segment_mid, segment_bl, segment_bot}:
            digits[2] = set(s)
        elif set(s) == {segment_top, segment_ur, segment_mid, segment_br, segment_bot}:
            digits[3] = set(s)
        elif set(s) == {segment_top, segment_ul, segment_mid, segment_br, segment_bot}:
            digits[5] = set(s)
        elif set(s) == {segment_top, segment_ul, segment_mid, segment_bl, segment_br, segment_bot}:
            digits[6] = set(s)
        elif set(s) == {segment_top, segment_ul, segment_ur, segment_mid, segment_br, segment_bot}:
            digits[9] = set(s)
    value = ''
    for o in output:
        if len(o) in [2, 3, 4, 7]:
            part1 += 1
        value += [str(k) for k, v in digits.items() if v == set(o)][0]
    part2 += int(value)

print('Part 1:', part1)
print('Part 2:', part2)
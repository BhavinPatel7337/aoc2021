from sys import path
import re
from math import ceil
from functools import reduce
from json import loads
from itertools import permutations

with open(path[0] + '/input.txt') as f:
    sf_numbers = f.read().splitlines()

def explode(s, pos, pair_len):
    pair = s[pos:pos + pair_len]
    l, r = [int(x) for x in re.search('\[(\d+),(\d+)\]', pair).groups()]
    s_l = s[:pos]
    s_r = s[pos + pair_len:]
    match_l = re.search('(\d+)([,\[\]]+)$', s_l)
    if match_l:
        s_l = s_l[:match_l.span()[0]] + str(int(match_l.group(1)) + l) + match_l.group(2)
    match_r = re.search('\d+', s_r)
    if match_r:
        s_r = s_r[:match_r.span()[0]] + str(int(match_r.group()) + r) + s_r[match_r.span()[1]:]
    return s_l + '0' + s_r

def shouldExplode(s):
    depth = 0
    i = 0
    while i < len(s):
        if s[i] == '[':
            if depth == 4:
                pair_len = 0
                while s[i] != ']':
                    pair_len += 1
                    i += 1
                return True, i - pair_len, pair_len + 1
            depth += 1
        elif s[i] == ']':
            depth -= 1
        i += 1
    return False, None, None

def sf_reduce(s):
    while True:
        e, pos, pair_len = shouldExplode(s)
        if e:
            s = explode(s, pos, pair_len)
            continue
        m = re.search('\d{2,}', s)
        if m:
            new_pair = '[' + str(int(m.group()) // 2) + ',' + str(ceil(int(m.group()) / 2)) + ']'
            s = s.replace(m.group(), new_pair, 1)
            continue
        break
    return s

def sf_add(a, b):
    return sf_reduce('[' + a + ',' + b + ']')

def magnitude(x):
    if isinstance(x, str):
        x = loads(x)
    if isinstance(x, int):
        return x
    if isinstance(x[0], list):
        x[0] = magnitude(x[0])
    if isinstance(x[1], list):
        x[1] = magnitude(x[1])
    return (3 * x[0]) + (2 * x[1])

print('Part 1:', magnitude(reduce(sf_add, sf_numbers)))
print('Part 2:', max([magnitude(sf_add(*p)) for p in permutations(sf_numbers, 2)]))
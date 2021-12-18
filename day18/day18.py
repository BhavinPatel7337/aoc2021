from sys import path
import re
from functools import reduce
from itertools import permutations

with open(path[0] + '/input.txt') as f:
    sf_numbers = f.read().splitlines()

def explode(s, pair, pair_start):
    s_l, s_r = s[pair_start - 1::-1], s[pair_start + len(pair):]
    v_l, v_r = [int(x) for x in re.search('\[(\d+),(\d+)\]', pair).groups()]
    m_l, m_r = [re.search('\d+', x) for x in [s_l, s_r]]
    if m_l:
        s_l = s_l.replace(m_l.group(), str(int(m_l.group()[::-1]) + v_l)[::-1], 1)
    if m_r:
        s_r = s_r.replace(m_r.group(), str(int(m_r.group()) + v_r), 1)
    return s_l[::-1] + '0' + s_r

def should_explode(s):
    depth = 0
    i = 0
    while i < len(s):
        if s[i] == '[':
            if depth == 4:
                pair = ''
                while s[i] != ']':
                    pair += s[i]
                    i += 1
                pair += s[i]
                return pair, i - len(pair) + 1
            depth += 1
        elif s[i] == ']':
            depth -= 1
        i += 1
    return None

def sf_reduce(s):
    while True:
        e = should_explode(s)
        if e:
            s = explode(s, *e)
            continue
        m = re.search('\d{2,}', s)
        if m:
            new_pair = '[' + str(int(m.group()) // 2) + ',' + str((int(m.group()) + 1) // 2) + ']'
            s = s.replace(m.group(), new_pair, 1)
            continue
        break
    return s

def sf_add(a, b):
    return sf_reduce('[' + a + ',' + b + ']')

def magnitude(s):
    return eval(s.replace('[', '(').replace(']', ')').replace(',', '*3+2*'))

print('Part 1:', magnitude(reduce(sf_add, sf_numbers)))
print('Part 2:', max([magnitude(sf_add(*p)) for p in permutations(sf_numbers, 2)]))
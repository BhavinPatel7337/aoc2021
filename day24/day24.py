from collections import deque
from sys import path

with open(path[0] + '/input.txt') as f:
    instructions = f.read().splitlines()

def monad_run(instructions, input_stack):
    ALU = {'w': 0, 'x': 0, 'y': 0, 'z':0}
    def get_val(b):
        if b in 'wxyz':
            return ALU[b]
        else:
            return int(b)
    for i in instructions:
        i = i.split()
        if i[0] == 'inp':
            if input_stack:
                inp = input_stack.popleft()
            else:
                inp = int(input())
            ALU[i[1]] = inp
        else:
            b = get_val(i[2])
            if i[0] == 'add':            
                ALU[i[1]] += b
            elif i[0] == 'mul':
                ALU[i[1]] *= b
            elif i[0] == 'div':
                ALU[i[1]] = ALU[i[1]] // b
            elif i[0] == 'mod':
                ALU[i[1]] %= b
            elif i[0] == 'eql':
                ALU[i[1]] = int(ALU[i[1]] == b)
    return not ALU['z']

def monad_decomp(digits, list_a, list_b):
    z = deque()
    for i in range(14):
        if z:
            x = z[-1]
        else:
            x = 0
        if list_a[i] < 0:
            z.pop()
        x += list_a[i]
        if x != digits[i]:
            y = digits[i] + list_b[i]
            z.append(y)
    return not len(z)

list_a = []
list_b = []
for n, i in enumerate(instructions):
    if n % 18 == 5:
        list_a.append(int(i.split()[-1]))
    elif n % 18 == 15:
        list_b.append(int(i.split()[-1]))

stack = deque()
largest = [0] * 14
smallest = [0] * 14
for i in range(14):
    if list_a[i] > 0:
        stack.append((i, list_b[i]))
    else:
        x = stack.pop()
        y = x[1] + list_a[i]
        if y > 0:
            largest[i] = 9
            largest[x[0]] = 9 - y
            smallest[i] = 1 + y
            smallest[x[0]] = 1
        elif y < 0:
            largest[x[0]] = 9
            largest[i] = 9 + y            
            smallest[x[0]] = 1 - y
            smallest[i] = 1
        else:
            largest[x[0]] = 9
            largest[i] = 9
            smallest[x[0]] = 1
            smallest[i] = 1

if monad_run(instructions, deque(largest)):
    print('Part 1:', ''.join([str(x) for x in largest]))

if monad_run(instructions, deque(smallest)):
    print('Part 2:', ''.join([str(x) for x in smallest]))
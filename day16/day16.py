from sys import path
from collections import deque
from math import prod

def hexToBin(h):
    return str(bin(int(h, 16)))[2:].zfill(4)

with open(path[0] + '/input.txt') as f: 
    bits = deque(''.join([hexToBin(x) for x in f.read().strip()]))

def getBits(n):
    return ''.join([bits.popleft() for _ in range(n)])

bit_count = 0

def parsePacket():
    global bit_count
    version = int(getBits(3), 2)
    type_id = int(getBits(3), 2)
    bit_count += 6
    if type_id == 4:
        cont = True
        value_string = ''
        while (cont):
            cont = bits.popleft() == '1'
            for _ in range(4):
                value_string += bits.popleft()
            bit_count += 5
        value = int(value_string, 2)
    else:
        length_id = bits.popleft()
        bit_count += 1
        sub_values = []
        if length_id == '0':
            length = int(getBits(15), 2)
            bit_count += 15
            sub_packet_end = bit_count + length
            while bit_count < sub_packet_end:
                sub_ver, sub_val = parsePacket()
                version += sub_ver
                sub_values.append(sub_val)
        elif length_id == '1':
            sub_packets = int(getBits(11), 2)
            bit_count += 11
            for _ in range(sub_packets):
                sub_ver, sub_val = parsePacket()
                version += sub_ver
                sub_values.append(sub_val)
        if type_id == 0:
            value = sum(sub_values)
        elif type_id == 1:
            value = prod(sub_values)
        elif type_id == 2:
            value = min(sub_values)
        elif type_id == 3:
            value = max(sub_values)
        elif type_id == 5:
            value = int(sub_values[0] > sub_values[1])
        elif type_id == 6:
            value = int(sub_values[0] < sub_values[1])
        elif type_id == 7:
            value = int(sub_values[0] == sub_values[1])
    return version, value

version_sum, total_value = parsePacket()
print('Part 1:', version_sum)
print('Part 2:', total_value)
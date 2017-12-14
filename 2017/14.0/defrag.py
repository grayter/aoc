#!/usr/bin/python

import sys
import operator

def khround(knot, pos, skip, moves):
    size = len(knot)
    for m in moves:
        if m > size:
            continue
        temp = knot * 2
        chunk = temp[pos:pos+m][::-1]
        knot[pos:pos+m] = chunk
        if pos+m >= size:
            knot[0:(pos+m)%size] = knot[size:pos+m]
            knot = knot[0:size]
        pos = (pos+m+skip) % size
        skip = skip + 1
    return (knot, pos, skip)

base = sys.argv[1]
ksize = int(sys.argv[2])
used = 0

for i in xrange(0, 128):
    row = base + "-" + str(i)
    knot = [i for i in xrange(0, ksize)]
    pos = 0
    skip = 0

    moves = [ord(x) for x in row] + [17,31,73,47,23]
    
    for i in xrange(0, 64):
        (knot, pos, skip) = khround(knot, pos, skip, moves)

    dense = []
    for i in xrange(0, 16):
        dense.append(reduce(operator.xor, knot[i*16:(i+1)*16], 0))

    for i in dense:
        used += bin(i).count("1")

print used

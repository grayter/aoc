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

ksize = int(sys.argv[2])
with open(sys.argv[1]) as f:
    raw = f.readlines()[0].strip()
    moves = [ord(x) for x in raw] + [17,31,73,47,23]
    knot = [i for i in xrange(0, ksize)]
    pos = 0
    skip = 0
    for i in xrange(0, 64):
        (knot, pos, skip) = khround(knot, pos, skip, moves)

    dense = []
    for i in xrange(0, 16):
        dense.append(reduce(operator.xor, knot[i*16:(i+1)*16], 0))

    for i in dense:
        sys.stdout.write("{0:0{1}x}".format(i, 2))

    print ""

#!/usr/bin/python

import sys

size = int(sys.argv[2])

with open(sys.argv[1]) as f:
    moves = map(int, f.readlines()[0].split(","))
    skip = 0
    pos = 0
    knot = [i for i in xrange(0, size)]

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
    
print knot
print knot[0] * knot[1]

#!/usr/bin/python

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

def knothash(val, size):
    knot = [x for x in xrange(0, size)]
    moves = [ord(x) for x in val] + [17,31,73,47,23]
    pos = 0
    skip = 0
    
    for j in xrange(0, 64):
        (knot, pos, skip) = khround(knot, pos, skip, moves)

    dense = []
    for j in xrange(0, 16):
        dense.append(reduce(operator.xor, knot[j*16:(j+1)*16], 0))

    hashval = []
    for j in dense:
        hashval.append("{0:0{1}x}".format(j, 2))

    return "".join(hashval)


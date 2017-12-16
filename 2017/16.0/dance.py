#!/usr/bin/python

import sys

def xcng(x, a, b):
    temp = x[a]
    x[a] = x[b]
    x[b] = temp
    return x

members = int(sys.argv[2])
positions = [chr(97+x) for x in xrange(0, members)]

with open(sys.argv[1]) as f:
    dance = f.readlines()[0].strip().split(",")
    
    for move in dance:
        if move[0] == 's':
            x = int(move[1:])
            positions = positions[-x:] + positions[:-x]
        elif move[0] == 'x':
            x, y = map(int, move[1:].split('/'))
            positions = xcng(positions, x, y)
        elif move[0] == 'p':
            i, j = move[1:].split('/')
            x = positions.index(i)
            y = positions.index(j)
            positions = xcng(positions, x, y)

print "".join(positions)

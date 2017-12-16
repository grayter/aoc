#!/usr/bin/python

import sys

def xcng(x, a, b):
    temp = x[a]
    x[a] = x[b]
    x[b] = temp
    return x

# Allow us to start on a different permutation
members = sys.argv[2].strip()
positions = [z for z in members]
print positions

with open(sys.argv[1]) as f:
    dance = f.readlines()[0].strip().split(",")

    again = []    
    for z in xrange(0, 1000000000):
        now = ''.join(positions)
        print z, now
        if now in again:
            # Detected a loop :) The remainder from the iter count
            # must be where we end up as repeating dance positions
            # makes everything else the same.
            print again[1000000000 % z]
            sys.exit(0)
            
        again.append(now)
            
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

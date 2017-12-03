#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    data = f.read()
    instructions = data.split(", ")

blocks = [0,0]
direction = 0
locations = set()
locations.add((0,0))

for dir in instructions:
    change = (1, 3)[dir[0] != "R"]
    direction = (direction + change) % 4;
    factor = (1, -1)[direction >= 2];
    amount = int(dir[1:])
    for i in range(0,amount):
        blocks[direction%2] += (1*factor)
        loc = (blocks[0], blocks[1])
        if loc in locations:
            print "Found dupe"
            print sum(map(abs, blocks))
            sys.exit(0)
        else:
            locations.add(loc)
    
blocks = map(abs, blocks)
print sum(blocks)

    
    
    



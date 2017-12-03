#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    data = f.read()
    instructions = data.split(", ")

blocks = [0,0]
direction = 0

for dir in instructions:
    change = (1, 3)[dir[0] != "R"]
    direction = (direction + change) % 4;
    factor = (1, -1)[direction >= 2];
    amount = int(dir[1:])
    blocks[direction%2] += (amount*factor)

blocks = map(abs, blocks)
print sum(blocks)

    
    
    



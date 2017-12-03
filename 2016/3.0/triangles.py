#!/usr/bin/python

import sys
import itertools

with open(sys.argv[1]) as f:
    bad = 0
    count = 0
    for line in f.readlines():
        val = [0,0,0]
        val[0] = int(line[0:5])
        val[1] = int(line[6:10])
        val[2] = int(line[11:15])
        count += 1
        for p in itertools.permutations(val):
            if(p[0] + p[1] <= p[2]):
                bad += 1
                break

    print count-bad
        

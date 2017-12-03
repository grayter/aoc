#!/usr/bin/python

import sys
import itertools




with open(sys.argv[1]) as f:
    bad = 0
    count = 0
    chunk = 0
    val = [[0,0,0],[0,0,0],[0,0,0]]

    for line in f.readlines():
        val[0][chunk] = int(line[0:5])
        val[1][chunk] = int(line[6:10])
        val[2][chunk] = int(line[11:15])
        count += 1
        chunk += 1
        if chunk == 3:
            for x in val:
                for p in itertools.permutations(x):
                    if(p[0] + p[1] <= p[2]):
                        bad += 1
                        break
            chunk = 0
            val = [[0,0,0],[0,0,0],[0,0,0]]

    print count-bad
        

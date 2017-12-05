#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    data = f.readlines()
    jump = [int(x) for x in data]
    pos = 0
    steps = 0
    while pos < len(jump):
        n = pos + jump[pos]
        jump[pos] += 1
        pos = n
        steps += 1

    print steps

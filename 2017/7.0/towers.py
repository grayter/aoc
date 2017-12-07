#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    data = f.readlines()
    discs = []
    supports = []
    for d in data:
        d = d.strip()
        if d.find("->") != -1:
            discs.append(d.split(" ")[0])
            supports.append(d.split("-> ")[1].split(", "))

    flat = [item for sublist in supports for item in sublist]
    for poss in discs:
        if not poss in flat:
            print poss


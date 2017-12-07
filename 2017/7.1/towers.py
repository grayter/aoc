#!/usr/bin/python

import sys


def tower_sum(tower_data, base):
    subtowers = tower_data[base][1]
    if len(subtowers) == 0:
        return tower_data[base][0]
    else:
        ts = []
        for st in subtowers:
            ts.append(tower_sum(tower_data, st))
        print "Tower base ", base, "self ", tower_data[base][0], "subs ", ts, "==", sum(ts)+tower_data[base][0]
        
        return sum(ts)+tower_data[base][0]

def find_base(tower_data):
    supports = []
    discs    = []
    for t in tower_data:
        if len(tower_data[t][1]) != 0:
            discs.append(t)
            supports.append(tower_data[t][1])
    flat = [item for sublist in supports for item in sublist]
    towers = []
    for poss in discs:
        if not poss in flat:
            return poss

with open(sys.argv[1]) as f:
    data = f.readlines()

    tower_data = {}
    for d in data:
        d = d.strip()
        if d.find("->") != -1:
            tower_data[d.split(" ")[0]] = (int(d.split(" ")[1][1:-1]), d.split("-> ")[1].split(", "))
        else:
            tower_data[d.split(" ")[0]] = (int(d.split(" ")[1][1:-1]), [])
    
    base = find_base(tower_data)
    tower_sum(tower_data, base)
    
        



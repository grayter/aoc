#!/usr/bin/python

import sys

fw = {}
with open(sys.argv[1]) as f:
    setup = f.readlines()
    for line in setup:
        a = line.strip()
        b = a.split(": ")
        fw[int(b[0])] = (0, int(b[1]), 1)

print fw

caught = []
for pico in xrange(0, int(max(fw, key=int))+1):
    if pico in fw:
        if fw[pico][0] == 0:
            caught.append(pico)

    for e in fw:
        if fw[e][0] == 0:
            fw[e] = (fw[e][0], fw[e][1], 1)
        elif fw[e][0] == fw[e][1]-1:
            fw[e] = (fw[e][0], fw[e][1], -1)
            
        fw[e] = ((fw[e][0] + fw[e][2]), fw[e][1], fw[e][2])

print fw
print caught
print sum([x*fw[x][1] for x in caught])

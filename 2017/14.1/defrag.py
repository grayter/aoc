#!/usr/bin/python

import sys
import operator
import kh

sectors = [[0 for x in xrange(128)] for x in xrange(128)] 
def explore(i, j):
    if sectors[i][j] == 1:
        sectors[i][j] = 'G'
        if i > 0:
            explore(i-1, j)
        if i < 127:
            explore(i+1, j)
        if j > 0:
            explore(i, j-1)
        if j < 127:
            explore(i, j+1)

base = sys.argv[1]
ksize = int(sys.argv[2])
used = 0

for i in xrange(0, 128):
    row = base + "-" + str(i)
    hashval = kh.knothash(row, ksize)

    for j in xrange(0, 32):
        binary = format(int(hashval[j],16), '04b')
        for b in xrange(0, len(binary)):
            sectors[i][(j*4)+b] = int(binary[b])

groups = 0
for i in xrange(0, 128):
    for j in xrange(0, 128):
        if not (sectors[i][j] == 'G' or sectors[i][j] == 0):
            groups += 1
            explore(i, j)

print groups

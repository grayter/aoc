#!/usr/bin/python

import sys

step = int(sys.argv[1])
pos = 0
val = 0

for i in xrange(1, 50000000+1):
    pos = (pos+step)%i
    if pos == 0:
        val = i
    
    pos = pos + 1
    
print val

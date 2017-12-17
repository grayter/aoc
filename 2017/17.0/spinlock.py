#!/usr/bin/python

import sys

sl = [0]

step = int(sys.argv[1])
pos = 0

for i in xrange(1, 2018):
    pos = (pos + step) % len(sl)
    sl.insert(pos+1, i)
    pos = pos + 1
    
idx = sl.index(2017)
idx = (idx+1) % len(sl)
print sl[idx]

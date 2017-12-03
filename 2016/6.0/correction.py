#!/usr/bin/python

import sys
from collections import Counter
data = []
with open(sys.argv[1]) as f:
    raw = f.readlines()
    length = len(raw[0])
    for i in xrange(0, length-1):
        column = [x[i] for x in raw]
        counter = Counter(column)
        data.append( counter.most_common(1)[0][0])

print "".join(data)

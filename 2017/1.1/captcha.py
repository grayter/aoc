#!/usr/bin/python

import sys

digits = sys.argv[1]
pairs = []

length = len(digits)
step   = length/2

for i in xrange(0, len(digits)):
    pairs.append(digits[i] + digits[(i+step)%length])

values = [int(x[0]) for x in pairs if x[0] == x[1]]
print sum(values)

#!/usr/bin/python

import sys

digits = sys.argv[1]
digits += digits[0]
pairs = []

for i in xrange(0, len(digits)-1):
    pairs.append(digits[i:i+2])

values = [int(x[0]) for x in pairs if x[0] == x[1]]
print sum(values)

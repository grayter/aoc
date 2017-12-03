#!/usr/bin/python

import os
import sys
import csv
import itertools
import fractions

with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

data = [[int(string) for string in inner] for inner in d]

checksums = []
for row in data:
    pairs = itertools.permutations(row, 2)
    divisible = [x[0]/x[1] for x in pairs if float(x[0])/x[1] == int(x[0]/x[1])]
    checksums.append(divisible[0])

print sum(checksums)
    

#!/usr/bin/python

import os
import sys
import csv

with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

data = [[int(string) for string in inner] for inner in d]

checksums = []
for row in data:
    mini = min(row)
    maxi = max(row)
    checksums.append(maxi-mini)

print sum(checksums)
    

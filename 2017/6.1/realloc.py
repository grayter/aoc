#!/usr/bin/python

import csv
import sys

with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter="\t")
    mem = [int(x) for x in list(reader)[0]]
    seen = {}
    distributions = 0
    represent = ",".join(map(str, mem))
    while not represent in seen:
        print represent
        seen[represent] = distributions
        index_max = max(xrange(len(mem)), key=mem.__getitem__)
        amount = mem[index_max]
        mem[index_max] = 0
        while amount != 0:
            index_max = (index_max + 1) % len(mem)
            mem[index_max] += 1
            amount -= 1
        distributions += 1
        represent = ",".join(map(str, mem))
    print distributions-seen[represent]

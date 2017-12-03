#!/usr/bin/python

import sys
from collections import Counter

def comp(vala, valb):
    if(vala[1] > valb[1]):
        return -1
    elif(vala[1] < valb[1]):
        return 1
    elif(vala[0] > valb[0]):
        return 1
    elif(vala[0] < valb[0]):
        return -1
    else:
        return 0

section_sum = 0
with open(sys.argv[1]) as f:
    rooms = f.readlines()
    for room in rooms:
        room = room.strip()
        sections = room.split("-")
        counter = Counter("".join(sections[:-1]))
        common = sorted(counter.most_common(), cmp=comp)
        checksum = "".join([x[0] for x in common])[0:5]
        (section, claim_check) = sections[-1][:-1].split("[")
        if checksum == claim_check:
            section_sum += int(section)

print section_sum

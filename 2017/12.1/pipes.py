#!/usr/bin/python

import sys

def getgroup(structure, start):
    group = set()
    pending = [str(start)]

    while len(pending) != 0:
        if not pending[0] in group:
            group.add(pending[0])
            pending += structure[pending[0]]
        else:
            pending = pending[1:]

    return str(sorted(group))

structure = {}
with open(sys.argv[1]) as f:
    d = f.readlines()
    for link in d:
        l = link.strip()
        pipe = l.split(" <-> ", 2)
        endpoints = pipe[1].split(", ")
        structure[pipe[0]] = endpoints

top = int(max(structure, key=int))
groups = set()

for i in xrange(0, top+1):
    groups.add(getgroup(structure, i))

print len(groups)

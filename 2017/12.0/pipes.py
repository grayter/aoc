#!/usr/bin/python

import sys

structure = {}

with open(sys.argv[1]) as f:
    d = f.readlines()
    for link in d:
        l = link.strip()
        pipe = l.split(" <-> ", 2)
        endpoints = pipe[1].split(", ")
        structure[pipe[0]] = endpoints

group = set()
pending = ["0"]

while len(pending) != 0:
    if not pending[0] in group:
        group.add(pending[0])
        pending += structure[pending[0]]
    else:
        pending = pending[1:]

print len(group)

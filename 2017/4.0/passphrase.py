#!/usr/bin/python

import sys

count = 0
with open(sys.argv[1]) as f:
    phrases = f.readlines()
    for phrase in phrases:
        phrase.strip()
        words = phrase.split()
        unique = set()
        for w in words:
            unique.add(w)
        if len(words) == len(unique):
            count = count + 1

print count

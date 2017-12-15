#!/usr/bin/python

import sys

def update(val, factor):
    pos = (val*factor) % (2**31-1)
    pos = (pos & 0x7fffffff) + (pos >> 31)
    if pos >> 31:
        pos -= 0x7fffffff

    return pos

def step(val,factor,check):
    pos = update(val, factor)
    while pos % check != 0:
        pos = update(pos, factor)
        
    return pos

A = int(sys.argv[1])
B = int(sys.argv[2])
print A
print B

judge = 0
for i in xrange(0, 5000000):
    A = step(A, 16807, 4)
    B = step(B, 48271, 8)

    if (A & 0xFFFF) == (B & 0xFFFF):
        judge += 1

print judge

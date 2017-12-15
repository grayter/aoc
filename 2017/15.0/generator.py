#!/usr/bin/python

import sys

def step(val,factor):
    return (val*factor) % (2**31-1)

def token(val):
    return bin(val)[-16:]

A = int(sys.argv[1])
B = int(sys.argv[2])
print A
print B

judge = 0
for i in xrange(0, 40000000):
    print i
    A = step(A, 16807)
    B = step(B, 48271)
    if (A & (2**16-1)) == (B & (2**16-1)):
        print "Match"
        judge += 1

print judge

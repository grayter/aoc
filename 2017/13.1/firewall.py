#!/usr/bin/python

import sys

fw = {}
with open(sys.argv[1]) as f:
    setup = f.readlines()
    for line in setup:
        a = line.strip()
        b = a.split(": ")
        fw[int(b[0])] = (0, int(b[1]), 1)

print fw

def advance(fw):
    for e in fw:
        if fw[e][0] == 0:
            fw[e] = (fw[e][0], fw[e][1], 1)
        elif fw[e][0] == fw[e][1]-1:
            fw[e] = (fw[e][0], fw[e][1], -1)
        
        fw[e] = ((fw[e][0] + fw[e][2]), fw[e][1], fw[e][2])

def getsCaught(fw):
    for pico in xrange(0, int(max(fw, key=int))+1):
        if pico in fw:
            if fw[pico][0] == 0:
                return True
        advance(fw)

    return False
    
        
done = False
delay = 0
next = fw.copy()
while not done:
    print delay    
    attempt = next.copy()
    print attempt
    next = attempt.copy()
        
    if not getsCaught(attempt):
        print delay
        sys.exit(0)
    else:
        delay = delay + 1
        advance(next)
        

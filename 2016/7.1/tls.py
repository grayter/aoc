#!/usr/bin/python

import sys
import re

def getABA(nets):
    aba = []
    for n in nets:
        for i in range(0, len(n)-2):
            if (n[i] == n[i+2]) and (n[i] != n[i+1]):
                aba.append(n[i:i+3])
    return aba

def checkBAB(hyper, option):
    for h in hyper:
        for i in xrange(0, len(h)-2):
            if (h[i] == h[i+2]) and (h[i+1] != h[i]):
                if(h[i] == option[1]) and (h[i+1] == option[0]):
                    return True
    return False

count = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()
    for addr in lines:
        hypernet = [x[1:-1] for x in re.findall("\[[^\]]+\]", addr.strip())]        
        nets = re.split("\[[^\]]*\]", addr.strip())
        aba = getABA(nets)
        
        for option in aba:
            if checkBAB(hypernet, option):
                count = count + 1
                break

print count

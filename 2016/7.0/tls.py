#!/usr/bin/python

import sys
import re

def detect(c):
    for i in xrange(0, len(c)-3):        
        if (c[i+0] != c[i+1]) and (c[i+0] == c[i+3]) and (c[i+1] == c[i+2]):
            return True
    return False

count = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()
    for addr in lines:
        hypernet = [x[1:-1] for x in re.findall("\[[^\]]+\]", addr.strip())]        
        nets = re.split("\[[^\]]*\]", addr.strip())
        hvalid = True
    
        for h in hypernet:
            if detect(h):
                hvalid = False
        
        nvalid = False
        for n in nets:
            if detect(n):
                nvalid = True

        if hvalid and nvalid:
            count = count + 1

print count

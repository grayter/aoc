#!/usr/bin/python

import hashlib
import sys

id = sys.argv[1]
code = ["X"] * 8
count = 0
    
for i in xrange(0, 8):
    print "Starting ", i
    done = False
    while not done:
        m = hashlib.md5()
        m.update(id + str(count))
        d = m.hexdigest()
        count = count + 1

        if d[0:5] == "00000" and int(d[5], 16) < 8 and code[int(d[5], 16)] == "X":
            print "Digit found ", d[6], " @ ", d[5]
            code[int(d[5],16)] = d[6]
            done = True

print "".join(code)

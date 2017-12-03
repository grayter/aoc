#!/usr/bin/python

import hashlib
import sys

id = sys.argv[1]
code = []
count = 0
    
for i in xrange(0, 8):
    print "Starting ", i
    done = False
    while not done:
        m = hashlib.md5()
        m.update(id + str(count))
        d = m.hexdigest()
        count = count + 1
        if d[0:5] == "00000":
            print "Digit found ", d[5]
            code.append(d[5])
            done = True

print "".join(code)

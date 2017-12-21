#!/usr/bin/python

import sys
import math

def rotate(rule, amount):
    x = list(rule)
    for i in xrange(0, amount):
        x = zip(*x[::-1])

    for i in xrange(0, len(x)):
        x[i] = "".join(x[i])
        
    return x

def patgen(rule):
    patterns = []
    chunks = rule.split('/')
    
    # The four possible rotations
    for i in xrange(0, 4):
        # Itself rotated
        x = rotate(chunks, i)
        patterns.append(x)
        
        # Vertical flip
        patterns.append(x[::-1])
        
        # Horizontal flip
        z = list(x)
        for j in xrange(0, len(z)):
            z[j] = z[j][::-1]
        patterns.append(z)

    return patterns

def splitter(image):
    subchunks = []
    li = len(image)
    si = 0
    if li % 2 == 0:
        si = 2
    elif li % 3 == 0:
        si = 3
    else:
        print "Bad size"
        sys.exit(1)

    for ver in xrange(0, li/si):
        for hor in xrange(0, li/si):
            chunk = list()
            for row in xrange(0, si):
                chunk.append(image[(ver*si)+row][hor*si:(hor+1)*si])
            subchunks.append(chunk)
            
    return subchunks

def merger(subchunks):
    li = len(subchunks)
    rows = int(math.sqrt(li * len(subchunks[0]) * len(subchunks[0])))
    image = [''] * rows

    scpr = rows / len(subchunks[0])
    for i in xrange(0, rows):
        for j in xrange(0, scpr):
            image[i] += subchunks[((i//len(subchunks[0]))*scpr)+j][i%len(subchunks[0])]

    return image
    
rules = {}

with open(sys.argv[1]) as f:
    data = f.readlines()
    for d in data:
        i = d.strip()
        info = i.split(" => ")
        patterns = patgen(info[0])
        for p in patterns:
            rules[str(p)] = info[1].split('/')

image = [".#.", "..#", "###"]
for i in rules:
    print i, "==>", rules[i]

iters = int(sys.argv[2])
    
for iterations in xrange(0, iters):
    size = len(image)
    subchunks = splitter(image)
    newchunks = []
    for sc in subchunks:
        if str(sc) in rules:
            newchunks.append(rules[str(sc)])
        else:
            print "Not in rulebook?"
            newchunks.append(sc)

    image = merger(newchunks)
    
on = 0
for i in image:
    on += i.count('#')

print on

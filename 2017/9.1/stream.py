#!/usr/bin/python

import sys

def sum_stream(stream):
    score = 1
    total = 0
    for c in stream:
        if c == "{":
            total += score
            score += 1
        elif c == "}":
            score -= 1
    return total
        
def drop_garbage(stream):
    junk = 0
    clean = []
    inRubbish = False
    ignore    = False
    for i in xrange(0, len(stream)):
        if ignore:
            ignore = False
        else:
            if not inRubbish and stream[i] != "<":
                clean.append(stream[i])
            elif not inRubbish and stream[i] == "<":
                inRubbish = True
            elif inRubbish and not ignore and stream[i] == ">":
                inRubbish = False
            elif inRubbish and not ignore and stream[i] == "!":
                ignore = True
            else:
                junk += 1
    print junk
    return "".join(clean)
        
with open(sys.argv[1]) as f:
    stream = f.readlines()[0].strip()    
    stream = drop_garbage(stream)

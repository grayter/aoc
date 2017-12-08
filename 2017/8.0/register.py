#!/usr/bin/python

import sys
import operator

def ensure(regs, reg):
    if not reg in regs:
        regs[reg] = 0

def conditional(regs, con):
    reg = con[0]
    val = int(con[2])
    if con[1] == ">":
        return regs[reg] > val
    elif con[1] == "<":
        return regs[reg] < val
    elif con[1] == ">=":
        return regs[reg] >= val
    elif con[1] == "<=":
        return regs[reg] <= val
    elif con[1] == "==":
        return regs[reg] == val
    elif con[1] == "!=":
        return regs[reg] != val

    return False

def apply(regs, req):
    reg = req[0]
    val = int(req[2])
    if req[1] == "inc":
        regs[reg] += val
    elif req[1] == "dec":
        regs[reg] -= val

    return

regs = {}
with open(sys.argv[1]) as f:
    d = f.readlines()
    for ins in d:
        ins = ins.strip()
        parts = ins.split(" ")
        req = parts[0:3]
        con = parts[4:7]
        ensure(regs, req[0])
        ensure(regs, con[0])
        if conditional(regs, con):
            apply(regs, req)

print regs
print max(regs.iteritems(), key=operator.itemgetter(1))[0]
print regs[max(regs.iteritems(), key=operator.itemgetter(1))[0]]

#!/usr/bin/python

import sys
from collections import defaultdict

registers = defaultdict(int)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def getVal(reg, x):
    if isInt(x):
        return int(x)
    else:
        return reg[x]
    
def operate(ins, reg):
    x = ins.split()
    if x[0] == "snd":
        print "Playing sound", getVal(reg, x[1])
        reg["SOUND"] = getVal(reg, x[1])
    elif x[0] == "set":
        reg[x[1]] = getVal(reg, x[2])
    elif x[0] == "add":
        reg[x[1]] += getVal(reg, x[2])
    elif x[0] == "mul":
        reg[x[1]] *= getVal(reg, x[2])
    elif x[0] == "mod":
        reg[x[1]] = reg[x[1]] % getVal(reg, x[2])
    elif x[0] == "rcv":
        if getVal(reg, x[1]) != 0:
            print "Recovering sound", reg["SOUND"]
    elif x[0] == "jgz":
        if getVal(reg, x[1]) > 0:
            reg["JUMP"] = getVal(reg, x[2])

    return reg
            
                
with open(sys.argv[1]) as f:
    data = f.readlines()
    i = 0
    while i < len(data):
        instruction = data[i].strip()
        registers = operate(instruction, registers)
        if registers["JUMP"] != 0:
            i += registers["JUMP"]
            registers["JUMP"] = 0
        else:
            i += 1
            
        print registers

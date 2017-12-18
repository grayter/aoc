#!/usr/bin/python

import sys
from collections import defaultdict

regA = defaultdict(int)
regA['p'] = 0
regB = defaultdict(int)
regB['p'] = 1

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
    
def operate(ins, reg, prog, queue):
    x = ins.split()
    if x[0] == "snd":
        print "Sending Value"
        queue[(prog+1)%2].append(getVal(reg,x[1]))
        reg["SENDING"] += 1
    elif x[0] == "set":
        reg[x[1]] = getVal(reg, x[2])
    elif x[0] == "add":
        reg[x[1]] += getVal(reg, x[2])
    elif x[0] == "mul":
        reg[x[1]] *= getVal(reg, x[2])
    elif x[0] == "mod":
        reg[x[1]] = reg[x[1]] % getVal(reg, x[2])
    elif x[0] == "rcv":
        print "Receiving value"
        if len(queue[prog]) != 0:
            reg[x[1]] = queue[prog].pop(0)
            reg["RECEIVED"] += 1
        else:
            reg["JUMP"] = 'X'
    elif x[0] == "jgz":
        if getVal(reg, x[1]) > 0:
            reg["JUMP"] = getVal(reg, x[2])

    return reg
            
                
with open(sys.argv[1]) as f:
    data = f.readlines()
    reg = regA
    iA = 0
    iB = 0
    i = 0
    prog = 0
    queues = [[],[]]
    
    while i < len(data):
        print "Running Prog", prog
        instruction = data[i].strip()
        registers = operate(instruction, reg, prog, queues)
        if reg["JUMP"] != 0:
            if registers["JUMP"] == 'X':
                reg["JUMP"] = 0
                print "Blocked"
                if prog == 0:
                    reg = regB
                    iA = i
                    i = iB
                    prog = 1
                else:
                    reg = regA
                    iB = i
                    i = iA
                    prog = 0
            else:
                i += registers["JUMP"]
                reg["JUMP"] = 0
        else:
            i += 1

        print "A", regA
        print "B", regB

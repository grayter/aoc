#!/usr/bin/python

import sys

def parse(data):
    elem = data[3:-1]
    elem = elem.split(",")
    elem = map(int, elem)
    return elem

def dist(pos):
    return sum(map(abs, pos[1]))

def minitem(swarm):
    (val, idx) = min(enumerate([x[0] for x in swarm]), key=dist)
    print val, idx
    return idx

def stepParticle(particle):
    for i in xrange(0, 3):
        particle[1][i] += particle[2][i]

    for i in xrange(0, 3):
        particle[0][i] += particle[1][i]

def stepSwarm(swarm):
    for p in swarm:
        stepParticle(p)

def removeCollisions(swarm):
    newSwarm = []
    for p in swarm:
        if len([x for x in swarm if x[0] == p[0]]) == 1:            
            newSwarm.append(p)
    return newSwarm
        
swarm = []

with open(sys.argv[1]) as f:
    data = f.readlines()
    for particle in data:
        particle = particle.strip()
        parts = particle.split(", ")
        pos = parse(parts[0])
        vel = parse(parts[1])
        acc = parse(parts[2])
        swarm.append([pos,vel,acc])
        
for i in xrange(0, 10000000):    
    print len(swarm)
    stepSwarm(swarm)
    swarm = removeCollisions(swarm)

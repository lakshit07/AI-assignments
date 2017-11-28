'''
NAME : Lakshit Bhutani
ID : 2014A&PS0095P
'''
from graph import *
from sets import Set

'''
Computes Markov blanket of variable v
'''
def markovBlanket(v):
    b = Set([v])
    p = allNodes[v].parent
    c = allNodes[v].children
    cp = []
    for i in c:
        for j in allNodes[i].parent:
            cp.append(j)
    for i in p:
        b.add(i)
    for i in c:
        b.add(i)
    for i in cp:
        b.add(i)
    return list(b)

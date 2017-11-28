from graph import *
from collections import deque

'''
Computes probability of node given assignment for parent
'''
def conditional(node, parent):
    ch = node
    n = allNodes[ch]
    ctr = 0
    for i in n.parent:
        for j in parent:
            if i == j:
                ctr = ctr * 2 + 1
                break
            elif i.lower() == j:
                ctr = ctr * 2
                break
    return n.prob[ctr]


'''
Produces topological sorting of nodes
'''
def tsort():
    vertex = []
    index = {}
    indegree = []
    outdegree = []
    j = 0

    for i in allNodes:
        vertex.append(allNodes[i].name)
        index[allNodes[i].name] = j
        j += 1
        indegree.append(len(allNodes[i].parent))
        outdegree.append(len(allNodes[i].children))

    q = deque()
    for i in range(0, len(vertex)):
        if indegree[i] == 0:
            q.append(i)
    order = []

    while q:
        u = q.pop()
        order.append(vertex[u])
        for i in allNodes[vertex[u]].children:
            indegree[index[i]] = indegree[index[i]] - 1
            if indegree[index[i]] == 0:
                q.append(index[i])
    return order
        

'''
Main method to compute consitional probability P(X | E)
'''
def calculate(X, E):
    s = len(X)
    if s == 0:
        return "No query variable found"
    for i in X:
        for j in E:
            if i.upper() == j.upper():
                return "Same variable " , i , "in both query and condition"
    topo_sort = tsort()
    if len(E) == 1 and E[0] == '':
        E=[]
    norm = 0
    for i in range(0, 2**s):
        temp = list(E)
        for j in range(0, s):
            if ((i & (1 << j) > 0)):
                temp.append(X[j].upper())
            else:
                temp.append(X[j].lower())
        val = calculate_util(topo_sort, temp)
        norm += val
    temp2 = E + X
    num = calculate_util(topo_sort, temp2)
    return float(num)/norm

'''
Checks for presence/absence of c in L
'''
def present(c, L):
    for i in L:
        if c == i:
            return 1
        elif c.lower() == i:
            return -1
    return 0

'''
computes joint probability of variables in L given ordering arr
'''
def calculate_util(arr, L):
    if len(arr) == 0:
        return 1
    f = arr[0]
    val = present(f, L)

    pars = allNodes[f].parent

    pars_val = []
    for i in pars:
        for j in L:
            if i == j:
                pars_val.append(j)
                break
            elif i.lower() == j:
                pars_val.append(j)
                break

    if val == 1:
        return conditional(f, pars_val) * calculate_util(arr[1:], L)
    elif val == -1:
        return (1 - conditional(f, pars_val)) * calculate_util(arr[1:], L)
    else:
        return (conditional(f, pars_val) * calculate_util(arr[1:], L + [f.upper()])) + ((1 - conditional(f, pars_val)) * calculate_util(arr[1:], L + [f.lower()]))

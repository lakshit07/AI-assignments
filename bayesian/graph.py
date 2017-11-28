'''
NAME : Lakshit Bhutani
ID : 2014A&PS0095P
'''
import re
allNodes = {}

'''
Bayesian Network Node structure
'''
class Node:
    def __init__(self, ch, par_list, prob_list):
        self.name = ch
        self.parent = par_list
        self.prob = prob_list
        self.children = []

    def __str__(self):
        a =  "Node: " + self.name
        b = "Children: " + str(self.children)
        c = "Probabilities: " + str(self.prob)
        d = "Parents: " + str(self.parent)
        return a + " " + b + " " + c + " " + d

    def appendChild(self, ch):
        if ch in self.children:
            pass
        else:
            self.children.append(ch)       

'''
Method to create the bayesian network from file fname
'''
def createBayesian(fname):
    f = open(fname, 'r')
    
    if f is None:
        print "File doesn't exist"

    else:
        for line in f:
            if line[0] == '$':
                break

            else:
                x = line.split('>>')
                root = x[0][0]
                par = []
                z = ""
                for i in range(2, len(x[1]) - 2):
                    z += x[1][i]
                if len(z) > 0:
                    temp = re.split(', ', z)
                    for i in temp:
                        if len(i) > 0:
                            par.append(i)
                temp = re.split(' |\n' , x[2])
                probs = []
                
                for i in temp:
                    if len(i) > 0:
                        probs.append(float(i))
            
                n = Node(root, par, probs)
                allNodes[n.name] = n
        
        f.close()       
        f = open(fname, 'r')
        for line in f:
            if line[0] == '$':
                break
            else:
                x = line.split('>>')
                root = x[0][0]
                par = []
                z = ""
                for i in range(2, len(x[1]) - 2):
                    z += x[1][i]
                if len(z) > 0:
                    temp = re.split(', ', z)
                    for i in temp:
                        if len(i) > 0:
                            par.append(i)
                for i in par:
                    allNodes[i].appendChild(root)

        f.close()       

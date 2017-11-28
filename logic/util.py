import sys
from cnf import *

def argmap(operator, funct, expr):
	a = (operator,)
	b = [funct(x) for x in expr[1:]]
	t = tuple(b)
	ans = a + t
	return ans

class VariableError (Exception):
    pass   

class countr:
    def __init__ (self, init_value = 0):
        self.val = init_value
    def next (self):
        cntr = self.val 
        self.val = self.val + 1
        return cntr

scounter = countr()
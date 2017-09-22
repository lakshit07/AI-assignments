'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

from math import floor
from random import sample

def generator(f, p):
	'''
	Generates p percent dirt
	'''
	n = f.n
	x = int(floor((p/100.0) * (n * n)))
	rnd = sample(range(0, int(n*n)), x)
	for i in rnd:
		row = i/n
		col = i%n
		f.AddDirt(row, col)
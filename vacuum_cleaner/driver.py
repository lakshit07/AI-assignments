'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

from utils import *
from dirtgenerator import *
from search import *
from analysis import *

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple	

def initialize(f):	
	'''
	Generated a random floor using p percent dirt
	'''
	print ("Enter the dirt percentage p = "),
	p = int(raw_input())
	if p < 0 or p > 100:
		print "Incorrect percentage value"
	else:	
		generator(f, p)
		DrawFloor(f)

def action(f, l):
	'''
	Returns action sequence corresponding to a path
	'''
	fl = f.tile
	visited = []
	ans = "R "
	px = 0
	py = 0
	for i in l:
		if px != i[0]:
			if i[0] > px:
				ans += "MD "
			else:
				ans += "MU "
			px = i[0]	
		elif py != i[1]:
			if i[1] > py:
				ans += "MR "
			else:
				ans += "ML "
			py = i[1]
		else:
			pass

		if fl[px][py] == 1 and (px, py) not in visited:
			ans += R + "S " + W
			visited.append((px, py))
	ans += "R"		
	return ans		



def main():
	'''
	Main Driver program
	'''
	print B + "\tVACUUM CLEANER AGENT" + W
	print R + "Uninformed search works for all dimensions but informed search works fine for N <= 5, works slow for N = 6 and very slow for N >= 7" + W
	print ("Enter dimension of floor (NxN) - N = "),
	n = int(raw_input())
	if n < 1:
		print "Incorrect floor dimensions"
		return
	else:	
		f = tilefloor(n)
		ans1 = []
		ans21 = []
		ans22 = []

	while(True):
		print (O + "\nOption 1: Display the room environment\n"
				"Option 2: Find the path (action sequence) and path cost using T1\n"
				"Option 3: Find the path (action sequence) and path cost using T2\n"
				"Option 4: Show all results and graphs in the GUI.\n"
				"Option 5: Quit\n" + W)	
		print G + "Choice : " + W,
		opt = int(raw_input())
		if opt == 1:
			initialize(f)
		elif opt == 2:
			stack = Stack()
			us = USearch(f, (0,0), stack)
			ans1 = us.UFind()
			if ans1 is None:
				print "No path found using uninformed search"
			else:
				print "PATH : " + str(ans1[3])
				print "ACTION SEQUENCE : " + action(f, ans1[3])
				print "COST : " + str( (len(ans1[3]) - 1)*2 + f.TotalDirt )
		elif opt == 3:
			pq = PriorityQueue()
			ins = ISearch(f, (0,0), pq)
			ans21 = ins.IFind(1)
			if ans21 is None:
				print "No path found using heuristic 1"
			else:
				print "PATH using h1: " + str(ans21[3])
				print "ACTION SEQUENCE : " + action(f, ans21[3])
				print "COST using h1: " + str( (len(ans21[3]) - 1)*2 + f.TotalDirt )
			while not pq.empty():
				pq.get(False)
			ans22 = ins.IFind(2)
			if ans22 is None:
				print "No path found using heuristic 2"
			else:
				print "PATH using h2: " + str(ans22[3])
				print "ACTION SEQUENCE : " + action(f, ans22[3])			
				print "COST using h2: " + str( (len(ans22[3]) - 1)*2 + f.TotalDirt )
			
		elif opt == 4:
			DrawAnalysis(f, ans1, ans21, ans22)		
		else:
			break 	


if __name__ == "__main__":
    main()
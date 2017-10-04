'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

from game import *
import time
s = tictactoe()

t1 = 0
t2 = 0
notim = 0
tgame = 0.0
mwin = 0
hwin = 0

def isValid(x, y):
	'''
	Check if the click made by the user at coordinates (x,y) is valid or not
	A valid move is within the grid and in the first empty row of a column
	'''
	if x < 100 or x > 500 or y > 200 or y < -200:
		return None
	else:
		if y >= 100:
			row = 0
		elif y >= 0:
			row = 1;
		elif y >= -100:
			row = 2
		else:
			row = 3

		if x <= 200:
			col = 0
		elif x <= 300:
			col = 1
		elif x <= 400:
			col = 2
		else:
			col = 3

		if s.state[row][col] != s.empty:
			return None
		else:
			flag = True
			for i in range(0, row):
				if s.state[i][col] == s.empty:
					flag = False
					break
			if flag:
				return (row, col)
			else:
				return None

def firstmove(c):
	'''
	Makes the first move of the machine according to the algorithm
	'''
	s.state = []
	s.player = 'X'
	s.opposition = 'O'
	for i in range(0, s.n):
		temp = []
		for j in range(0, s.n):
			temp.append(s.empty)
		s.state.append(temp)

	x = tuple(s.mytuple(s.state))
	if c == 0:
		val = util[x]
		global t1
		t1 = time.time()
	else:
		val = utilab[x]	
		global t2
		t2 = time.time()
	move = val[1]
	xm = move[0]
	ym = move[1]
	s.mark(xm, ym, 1)
	s.state[xm][ym] = s.player


def mrk(z):
	'''
	Displays the line over the three circles leading to the win/loss
	'''
	pen(fillcolor="black", pencolor="brown", pensize=3)
	c = []
	for p in z:
		x = p[0]
		y = p[1]
		c.append((150 + 100*y, 150 - 100*x))
	pu()
	goto(c[0][0], c[0][1])
	pd()
	for i in range(1, len(c)):
		goto(c[i][0], c[i][1])
	pu()		


def showresult(a, p = None):
	'''
	Displays WIN/ LOSS/ TIE of the current game
	'''
	onscreenclick(None)
	global hwin
	global mwin
	global tgame
	tgame += 1
	if a == -1:
		pen(fillcolor="black", pencolor="red", pensize=3)
		pu()
		goto(250, -300)
		pd()
		write("You LOSE" , font=("Arial", 20, "normal"))
		mwin += 1
		mrk(p)
	elif a == 1:
		pen(fillcolor="black", pencolor="green", pensize=3)
		pu()
		goto(250, -300)
		pd()
		write("You WIN" , font=("Arial", 20, "normal"))
		hwin += 1
		z = s.win()
		mrk(p)
	else:
		pen(fillcolor="black", pencolor="green", pensize=3)
		pu()
		goto(250, -300)
		pd()
		write("Game Tied" , font=("Arial", 20, "normal"))		


def findmark(x, y):
	'''
	OnClick listener which check the validity of the move and places the appropriate mark on the tile
	It also makes the next machine move accordingly.
	'''
	z = isValid(x, y)
	global notim
	if z is not None:
		row = z[0]
		col = z[1]
		s.mark(row, col, 0)
		s.state[row][col] = s.opposition
		if s.checkwin(0) is not None:
			showresult(1, s.checkwin(0))
			r[4] = time.time() - t1
			r[10] += r[4]
			notim += 1
		elif s.tied():
			showresult(0)
			r[4] = time.time() - t1
			r[10] += r[4]
			notim += 1	
		else:
			x = tuple(s.mytuple(s.state))
			val = util[x]
			move = val[1]
			xm = move[0]
			ym = move[1]
			s.mark(xm, ym, 1)
			s.state[xm][ym] = s.player

			if s.checkwin(1) is not None:
				showresult(-1, s.checkwin(1))
				r[4] = time.time() - t1
				r[10] += r[4]
				notim += 1
			elif s.tied():
				showresult(0)
				r[4] = time.time() - t1
				r[10] += r[4]
				notim += 1

def findmarkab(x, y):
	'''
	OnClick listener which check the validity of the move and places the appropriate mark on the tile
	It also makes the next machine move accordingly.
	'''
	global notim
	z = isValid(x, y)
	if z is not None:
		row = z[0]
		col = z[1]
		s.mark(row, col, 0)
		s.state[row][col] = s.opposition
		if s.checkwin(0) is not None:
			showresult(1, s.checkwin(0))
			r[8] = time.time() - t2
			r[10] += r[8]
			notim += 1
		elif s.tied():
			showresult(0)
			r[8] = time.time() - t2
			r[10] += r[8]
			notim += 1	
		else:
			x = tuple(s.mytuple(s.state))
			val = utilab[x]
			move = val[1]
			xm = move[0]
			ym = move[1]
			s.mark(xm, ym, 1)
			s.state[xm][ym] = s.player

			if s.checkwin(1) is not None:
				showresult(-1, s.checkwin(1))
				r[8] = time.time() - t2
				r[10] += r[8]
				notim += 1
			elif s.tied():
				showresult(0)
				r[8] = time.time() - t2
				r[10] += r[8]
				notim += 1		

def analysis():
	'''
	Displays the relevant information on the left panel
	'''
	pen(fillcolor="black", pencolor="black", pensize=2)
	
	# Minimax Analysis
	pu()
	goto(-450, 300)
	pd()
	write("Minimax algorithm based analysis", font=("Arial", 14, "bold"))
	pu()
	goto(-500, 260)
	pd()
	write("Number of distinct nodes generated : %d [Overall nodes : 7262072]" % r[1], font=("Arial", 10, "normal"))
	pu()
	goto(-500, 230)
	pd()
	write("Memory allocated to one node : %d bytes" % r[2], font=("Arial", 10, "normal"))
	pu()
	goto(-500, 200)
	pd()
	write("Maximum growth of search tree : %d levels" % r[3], font=("Arial", 10, "normal"))
	pu()
	goto(-500, 170)
	pd()
	write("Total time to play the game : {} seconds" . format(r[4]), font=("Arial", 10, "normal"))
	pu()
	goto(-500, 140)
	pd()
	write("Number of nodes generated in 1 microsecond: {}" . format(r[5]), font=("Arial", 10, "normal"))
	pu()

	# Alpha Beta Analysis
	goto(-450, 70)
	pd()
	write("Alpha Beta pruning based analysis", font=("Arial", 14, "bold"))
	pu()
	goto(-500, 30)
	pd()
	write("Number of nodes generated : %d " % r[6], font=("Arial", 10, "normal"))
	pu()
	goto(-500, 0)
	pd()
	write("Saving using Pruning : {} % " . format(((7262072 - r[6]) / 7262072) * 100), font=("Arial", 10, "normal"))
	pu()
	goto(-500, -30)
	pd()
	write("Total time to play the game : {} seconds" . format(r[8]), font=("Arial", 10, "normal"))
	pu()

	# Comparative Analysis
	goto(-450, -100)
	pd()
	write("Comparative analysis", font=("Arial", 14, "bold"))
	pu()
	goto(-500, -140)
	pd()
	write("Memory used in minimax : {} bytes " .format(r[2]*r[3]), font=("Arial", 10, "normal"))
	pu()
	goto(-500, -160)
	pd()
	write("Memory used in alpha-beta pruning : {} bytes " .format(r[2]*r[3]), font=("Arial", 10, "normal"))
	pu()
	goto(-500, -200)
	pd()
	write("Average time to play the game : {} seconds" . format(r[10] / notim), font=("Arial", 10, "normal"))
	pu()
	goto(-500, -230)
	pd()
	write("Number of times M wins in 10 games : %d " % ((mwin/tgame) * 10) , font=("Arial", 10, "normal"))
	pu()
	goto(-500, -260)
	pd()
	write("Number of times M wins in 200 games : %d " % ((mwin/tgame) * 200) , font=("Arial", 10, "normal"))
	pu()

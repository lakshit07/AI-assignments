from game import *

s = tictactoe()

def isValid(x, y):
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

def firstmove():
	s.clear()
	x = tuple(s.mytuple(s.state))
	val = util[x]
	move = val[1]
	xm = move[0]
	ym = move[1]
	s.mark(xm, ym, 1)
	s.state[xm][ym] = s.player


def showresult(a):
	if a == -1:
		pen(fillcolor="black", pencolor="red", pensize=3)
		write("You LOSE" , font=("Arial", 10, "normal"))


def findmark(x, y):
	z = isValid(x, y)
	if z is not None:
		r = z[0]
		c = z[1]
		s.mark(r, c, 0)
		s.state[r][c] = s.opposition
		x = tuple(s.mytuple(s.state))
		val = util[x]
		if val[1] is None:
			if val[0] == 0:
				showresult(0)
			elif val[0] == 1:
				showresult(-1)
			else:
				showresult(1)
		else:
			move = val[1]
			xm = move[0]
			ym = move[1]
			s.mark(xm, ym, 1)
			s.state[xm][ym] = s.player

			x = tuple(s.mytuple(s.state))
			val = util[x]

			if val[1] is None:
				if val[0] == 0:
					showresult(0)				
				elif val[0] == 1:
					showresult(-1)
				else:
					showresult(1)

from turtle import *
from copy import deepcopy
import time

util = {}
utilab = {}
r = []
for i in range(0, 15):
	r.append(0.0)

class tictactoe:
	def __init__(self, other = None):
		self.state = []
		self.player = 'X'
		self.opposition = 'O'
		self.empty = '.'
		self.n = 4
		for i in range(0, self.n):
			temp = []
			for j in range(0, self.n):
				temp.append(self.empty)
			self.state.append(temp)	
		if other:
			self.__dict__ = deepcopy(other.__dict__)	

	def clear(self):
		for i in range(0, self.n):
			temp = []
			for j in range(0, self.n):
				temp.append(self.empty)
			self.state.append(temp)				

	def move(self, x, y):
		game = tictactoe(self)
		game.state[x][y] = game.player
		(game.player, game.opposition) = (game.opposition, game.player)
		return game

	def mytuple(self, l):
		m = []
		for i in l:
			m.append(tuple(i))
		return m

	def minimaxab(self, player, alpha = -1000, beta = 1000):
		r[6] += 1
		if self.win():
			if player:
				fans = (-1, None)
			else:	
				fans = (1, None)
		elif self.tied():
			fans = (0, None)
		elif player:
			ans = (-2, None)
			flag = True
			for j in range(0, 4):
				for i in range(0, 4):
					if self.state[i][j] == self.empty:
						nextstate = self.move(i, j)						
						if tuple(self.mytuple(nextstate.state)) not in utilab:
							v = nextstate.minimaxab(not player, alpha, beta)[0]
						else:
							v = utilab[tuple(self.mytuple(nextstate.state))][0]
						if v > ans[0]:
							ans = (v, (i, j))
						if ans[0] >= beta:
							flag = False
							break
						alpha = max(alpha, ans[0])							
						break
				if not flag:
					break		
			fans = ans
		else:
			ans = (2, None)
			flag = True
			for j in range(0, 4):
				for i in range(0, 4):
					if self.state[i][j] == self.empty:
						nextstate = self.move(i, j)
						if tuple(self.mytuple(nextstate.state)) not in utilab:
							v = nextstate.minimaxab(not player, alpha, beta)[0]
						else:
							v = utilab[tuple(self.mytuple(nextstate.state))][0]
						if v < ans[0]:
							ans = (v, (i, j))
						if ans[0] <= alpha:
							flag = False
							break
						beta = min(beta, ans[0])
						break
				if not flag:
					break					
			fans = ans

		utilab[tuple(self.mytuple(self.state))] = fans
		return fans	
			

	def minimax(self, player, ht):
		r[1] += 1
		r[3] = max(r[3], ht)
		if self.win():
			if player:
				fans = (-1, None)
			else:	
				fans = (1, None)
		elif self.tied():
			fans = (0, None)
		elif player:
			ans = (-2, None)
			for j in range(0, 4):
				for i in range(0, 4):
					if self.state[i][j] == self.empty:
						nextstate = self.move(i, j)
						if tuple(self.mytuple(nextstate.state)) not in util:
							v = nextstate.minimax(not player, ht + 1)[0]
							if v > ans[0]:
								ans = (v, (i, j))
						else:
							v = util[tuple(self.mytuple(nextstate.state))][0]
							if v > ans[0]:
								ans = (v, (i, j))
						break
			fans = ans
		else:
			ans = (2, None)
			for j in range(0, 4):
				for i in range(0, 4):
					if self.state[i][j] == self.empty:
						nextstate = self.move(i, j)
						if tuple(self.mytuple(nextstate.state)) not in util:
							v = nextstate.minimax(not player, ht + 1)[0]
							if v < ans[0]:
								ans = (v, (i, j))
						else:
							v = util[tuple(self.mytuple(nextstate.state))][0]
							if v < ans[0]:
								ans = (v, (i, j))		
						break			
			fans = ans

		util[tuple(self.mytuple(self.state))] = fans
		return fans	

	def bestmove(self):
		t1 = time.time()
		self.minimax(True, 1)
		t2 = time.time()
		r[5] = r[1] / (t2 - t1)
		r[5] = r[5] / 1e6

	def bestmoveab(self):
		self.minimaxab(True)							

	def tied(self):
		for i in range(self.n):
			for j in range(self.n):
				if self.state[i][j] == self.empty:
					return False
		return True

	def checkwin(self, z):
		if z == 1:
			ch = 'X'
		else:
			ch = 'O'	
		# horizontal
		for i in range(0, self.n):
			for j in range(0, 2):
				row = []
				for k in range(0, 3):
					if self.state[i][j + k] == ch:
						row.append((i, j + k))
					if len(row) == 3:
						return row
		#vertical
		for j in range(0, self.n):
			for i in range(0, 2):
				col = []
				for k in range(0, 3):
					if self.state[i + k][j] == ch:
						col.append((i + k, j))
					if len(col) == 3:
						return col
		
		#diagonalLtoR
		diag = []
		for i in range(0, 3):
			j = i + 1
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag

		diag = []
		for i in range(0, 3):
			j = i
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		diag = []
		for i in range(1, 4):
			j = i
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		diag = []
		for i in range(1, 4):
			j = i - 1
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	


		#diagonalRtoL
		diag = []
		for i in range(0, 3):
			j = 2 - i
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag

		diag = []
		for i in range(0, 3):
			j = 3 - i
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		for i in range(1, 4):
			j = 3 - i
			diag = []
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		diag = []
		for i in range(1, 4):
			j = 4 - i
			if self.state[i][j] == ch:
				diag.append((i, j))
		if len(diag) == 3:
			return diag											

		return None	
		
	def win(self):
		# horizontal
		for i in range(0, self.n):
			for j in range(0, 2):
				row = []
				for k in range(0, 3):
					if self.state[i][j + k] == self.opposition:
						row.append((i, j + k))
					if len(row) == 3:
						return row
		#vertical
		for j in range(0, self.n):
			for i in range(0, 2):
				col = []
				for k in range(0, 3):
					if self.state[i + k][j] == self.opposition:
						col.append((i + k, j))
					if len(col) == 3:
						return col
		
		#diagonalLtoR
		diag = []
		for i in range(0, 3):
			j = i + 1
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag

		diag = []
		for i in range(0, 3):
			j = i
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		diag = []
		for i in range(1, 4):
			j = i
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		diag = []
		for i in range(1, 4):
			j = i - 1
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	


		#diagonalRtoL
		diag = []
		for i in range(0, 3):
			j = 2 - i
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag

		diag = []
		for i in range(0, 3):
			j = 3 - i
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		for i in range(1, 4):
			j = 3 - i
			diag = []
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag	
			
		diag = []
		for i in range(1, 4):
			j = 4 - i
			if self.state[i][j] == self.opposition:
				diag.append((i, j))
		if len(diag) == 3:
			return diag											

		return None

	def __str__(self):
	    string = ''
	    for x in range(self.n):
	      for y in range(self.n):
	        string += self.state[x][y]
	      string+="\n"
	    string += "----------\n"  
	    return string	


	def display(self):
		wn = Screen()
 		wn.title("Align3 game")  
		setup (width=1200, height=700, startx=0, starty=0)
		pen(fillcolor="black", pencolor="black", pensize=2)
		speed(100)
		pu()
		goto(0, 350)
		pd()
		goto(0, -350)
		pu()

		for i in range(0, 5):
			goto(100, 200-100*i)
			pd()
			goto(500, 200-100*i)
			pu()

		for i in range(0, 5):
			goto(100 + 100*i, 200)
			pd()
			goto(100 + 100*i, -200)
			pu()


	def mark(self, r, c, chance):
		if chance == 1:
			pen(fillcolor="green", pencolor="black", pensize=2)
			pu()
			goto(150 + 100*c, 100 - 100*r)
			pd()
			begin_fill()
			circle(50)
			end_fill()
			pu()
		else:
			pen(fillcolor="blue", pencolor="black", pensize=2)
			pu()
			goto(150 + 100*c, 100 - 100*r)
			pd()
			begin_fill()
			circle(50)
			end_fill()
			pu()

'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

from turtle import *
from copy import deepcopy
import time

util = {}
utilab = {}
r = []
for i in range(0, 15):
	r.append(0.0)

class tictactoe:
	'''
	Main class with state information - attributes and various functionalities
	'''
	def __init__(self, other = None):
		'''
		State constructor - initializes with initial state values
		'''
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
		'''
		Clears the board for new game
		'''
		for i in range(0, self.n):
			temp = []
			for j in range(0, self.n):
				temp.append(self.empty)
			self.state.append(temp)				

	def move(self, x, y):
		'''
		Makes the move at row x and column y
		Also changes the turn of the players
		'''
		game = tictactoe(self)
		game.state[x][y] = game.player
		(game.player, game.opposition) = (game.opposition, game.player)
		return game

	def mytuple(self, l):
		'''
		Converts list to tuple as python dictionary hashes only immutables 
		'''
		m = []
		for i in l:
			m.append(tuple(i))
		return m

	def minimaxab(self, player, alpha = -1000, beta = 1000):
		'''
		Basic minimax algorithm with alpha beta pruning
		'''
		r[6] += 1
		if self.terminal_test():
			if self.win():
				if player:
					fans = (-1, None)
				else:	
					fans = (1, None)
			else:
				fans = (0, None)
		elif player:
			ans = (-2, None)
			for i,j in self.successor_function():
				nextstate = self.move(i, j)						
				v = nextstate.minimaxab(not player, alpha, beta)[0]
				if v > ans[0]:
					ans = (v, (i, j))
				if ans[0] >= beta:
					break
				alpha = max(alpha, ans[0])				
			fans = ans
		else:
			ans = (2, None)
			for i,j in self.successor_function():
				nextstate = self.move(i, j)
				v = nextstate.minimaxab(not player, alpha, beta)[0]
				if v < ans[0]:
					ans = (v, (i, j))
				if ans[0] <= alpha:
					break
				beta = min(beta, ans[0])				
			fans = ans

		utilab[tuple(self.mytuple(self.state))] = fans
		return fans

	def terminal_test(s):
		'''
		Check the temrinal state - WIN / LOSS / TIE
		'''
		if s.win() or s.tied():
			return True;
		else:
			return False

	def successor_function(s):
		'''
		Generates the successors of a state
		Successors are the first non empty row of each of the column
		'''
		succ = []
		for j in range(0, s.n):
			for i in range(0, s.n):
				if s.state[i][j] == s.empty:
					succ.append((i, j))
					break
		return succ			
			

	def minimax(self, player, ht):
		'''
		Basic Minimax algorithm
		'''
		r[1] += 1
		r[3] = max(r[3], ht)

		if self.terminal_test():
			if self.win():
				if player:
					fans = (-1, None)
				else:	
					fans = (1, None)
			else:
				fans = (0, None)
		elif player:
			ans = (-2, None)
			for i,j in self.successor_function():
				nextstate = self.move(i, j)
				if tuple(self.mytuple(nextstate.state)) not in util:
					v = nextstate.minimax(not player, ht + 1)[0]
					if v > ans[0]:
						ans = (v, (i, j))
				else:
					v = util[tuple(self.mytuple(nextstate.state))][0]
					if v > ans[0]:
						ans = (v, (i, j))
			fans = ans
		else:
			ans = (2, None)
			for i,j in self.successor_function():
				nextstate = self.move(i, j)
				if tuple(self.mytuple(nextstate.state)) not in util:
					v = nextstate.minimax(not player, ht + 1)[0]
					if v < ans[0]:
						ans = (v, (i, j))
				else:
					v = util[tuple(self.mytuple(nextstate.state))][0]
					if v < ans[0]:
						ans = (v, (i, j))					
			fans = ans

		util[tuple(self.mytuple(self.state))] = fans
		return fans	

	def bestmove(self):
		'''
		Computes the moves (game tree) for minimax algorithm
		'''
		t1 = time.time()
		self.minimax(True, 1)
		t2 = time.time()
		r[5] = r[1] / (t2 - t1)
		r[5] = r[5] / 1e6

	def bestmoveab(self):
		'''
		Computes the moves (game tree) for alpha beta pruning
		'''
		self.minimaxab(True)

	def tied(self):
		'''
		Checks if the game is TIED
		'''
		for i in range(self.n):
			for j in range(self.n):
				if self.state[i][j] == self.empty:
					return False
		return True

	def checkwin(self, z):
		'''
		Checks if either of the player has WON
		'''
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
		'''
		Checks if either of the player has WON
		'''
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

	def display(self):
		'''
		Display the initial board configuration
		'''
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

		goto(250, 250)
		write("Base Line", font=("Arial", 10, "bold"))
		pu()
		pen(fillcolor="black", pencolor="red", pensize=8)
		goto(50, 225)
		pd()
		goto(550, 225)
		pu()
		pen(fillcolor="black", pencolor="black", pensize=2)

		for i in range(0, 5):
			goto(100, 200-100*i)
			pd()
			goto(500, 200-100*i)
			pu()
			if i < 4:
				goto(50, 150 - 100*i)
				pd()
				write("R{}".format(i + 1), font=("Arial", 12, "bold"))
				pu()


		for i in range(0, 5):
			goto(100 + 100*i, 200)
			pd()
			goto(100 + 100*i, -200)
			pu()
			if i < 4:
				goto(150 + 100*i, -250)
				pd()
				write("C{}".format(i + 1), font=("Arial", 12, "bold"))
				pu()					


	def mark(self, r, c, chance):
		'''
		Marks the appropriate tile with a circle corresponding to each player
		'''
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

'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

import sys
import time
from math import *

class UStateSpace():
	'''
	Uninformed search State space
	'''
	
	def __init__(self, f, pos):
		self.grid = f.tile
		self.pos = pos
		self.r = self.c = f.n
		self.dirt = f.TotalDirt

	def GetStartState(self):
		if self.grid[0][0] == 0:
			return [self.pos, [self.pos], 0] 		# Initial pos, path taken and dirt cleaned
		else:
			return [self.pos, [self.pos], 1]	

	def IsGoal(self, state):
		if state[2] == self.dirt:
			return True
		else:
			return False	

		
	def GetSuccessor(self, state):
		pos = state[0]
		path = state[1]
		cleaned = state[2]
		nextmoves = []
		cx = pos[0]
		cy = pos[1]

		def GetMove(x, y):
			move = (x, y)
			if move not in path:
				clean = cleaned
				if self.grid[x][y] == 1:
					clean += 1
				newPath = list(path)
				newPath.append(move)
				nextmoves.append((move, newPath, clean))

		if cx > 0:
			GetMove(cx - 1, cy)
		if cx < self.r - 1:
			GetMove(cx + 1, cy)
		if cy > 0:
			GetMove(cx, cy - 1)
		if cy < self.c - 1:
			GetMove(cx, cy + 1)	
		return nextmoves

	def alter(self, l):
		end = l[len(l) - 1]
		corners = [(0,0), (0, self.c - 1), (self.r - 1, 0), (self.r - 1, self.c - 1)]
		dist = []
		i = 0
		for p in corners:
			dist.append((abs(end[0] - p[0]) + abs(end[1] - p[1]) , i))
			i += 1
		dest = corners[min(dist)[1]]
		(x1, y1) = end
		(x2, y2) = dest

		for i in range(x1 + 1, x2 + 1):
			l.append((i, y1))
		for i in range(x1 - 1, x2 - 1, -1):
			l.append((i, y1))

		x = l[len(l) - 1][0]		
		for i in range(y1 + 1, y2 + 1):
			l.append((x, i))
		for i in range(y1 - 1, y2 - 1, -1):
			l.append((x, i))	

		return l					
	

class USearch(UStateSpace):
	'''
	Uninformed search implementation
	'''
	
	def __init__(self, f, pos, strategy):
		UStateSpace.__init__(self, f, pos)
		self.strategy = strategy

	def UFind(self):
		startTime = time.time()
		nodesGen = 0
		maxSize = 0
		maxLen = 0
		mem = 0
		self.strategy.push(self.GetStartState())
		while not self.strategy.empty():
			node = self.strategy.pop()
			maxSize = max(maxSize, sys.getsizeof(node))
			maxLen = max(maxLen, self.strategy.getsize())
			if self.IsGoal(node):
				endTime = time.time()
				return [nodesGen, maxSize, maxLen, self.alter(node[1]), endTime - startTime, mem]
			for move in self.GetSuccessor(node):
				nodesGen += 1
				self.strategy.push(move)
				mem += sys.getsizeof(move)
		return None			


class IStateSpace():
	'''
	Informed search State space
	'''
	
	def __init__(self, f, pos):
		self.grid = f.tile
		self.pos = pos
		self.r = self.c = f.n
		self.dirt = f.TotalDirt

	def GetStartState(self):
		if self.grid[0][0] == 0:
			return [0, self.pos, [self.pos], 0] 		# Heuristic value, Initial pos, path taken and dirt cleaned
		else:
			return [-50, self.pos, [self.pos], 1]	

	def IsGoal(self, state):
		if state[3] == self.dirt:
			return True
		else:
			return False

	def h2(self, x, y):
		hvalue = 0
		if self.grid[x][y] == 1:
			hvalue += 2
		if x > 0 and self.grid[x - 1][y] == 1:
			hvalue += 1
		if x < self.r - 1 and self.grid[x + 1][y] == 1:
			hvalue += 1
		if y > 0 and self.grid[x][y - 1] == 1:
			hvalue += 1
		if y < self.c - 1 and self.grid[x][y + 1] == 1:
			hvalue += 1
		return -hvalue

	def h1(self, x, y):
		hvalue = x + y - self.h2(x, y)
		return -hvalue
		
	def GetSuccessor(self, state, hval):
		pos = state[1]
		path = state[2]
		cleaned = state[3]
		nextmoves = []
		cx = pos[0]
		cy = pos[1]

		def GetMove(x, y):
			if (x,y) not in path:
				move = (x, y)
				clean = cleaned
				if self.grid[x][y] == 1 and (x, y) not in path:
					clean += 1
				newPath = list(path)
				newPath.append(move)
				if hval == 1:
					nextmoves.append((self.h1(x, y), move, newPath, clean))
				else:
					nextmoves.append((self.h2(x, y), move, newPath, clean))

		if cx > 0:
			GetMove(cx - 1, cy)
		if cx < self.r - 1:
			GetMove(cx + 1, cy)
		if cy > 0:
			GetMove(cx, cy - 1)
		if cy < self.c - 1:
			GetMove(cx, cy + 1)	
		
		return nextmoves


	def alter(self, l):
		end = l[len(l) - 1]
		corners = [(0,0), (0, self.c - 1), (self.r - 1, 0), (self.r - 1, self.c - 1)]
		dist = []
		i = 0
		for p in corners:
			dist.append((abs(end[0] - p[0]) + abs(end[1] - p[1]) , i))
			i += 1
		dest = corners[min(dist)[1]]
		(x1, y1) = end
		(x2, y2) = dest

		for i in range(x1 + 1, x2 + 1):
			l.append((i, y1))
		for i in range(x1 - 1, x2 - 1, -1):
			l.append((i, y1))

		x = l[len(l) - 1][0]		
		for i in range(y1 + 1, y2 + 1):
			l.append((x, i))
		for i in range(y1 - 1, y2 - 1, -1):
			l.append((x, i))	

		return l					



class ISearch(IStateSpace):
	'''
	Informed search implementation
	'''

	def __init__(self, f, pos, strategy):
		IStateSpace.__init__(self, f, pos)
		self.strategy = strategy


	def alter(self, l):
		end = l[len(l) - 1]
		corners = [(0,0), (0, self.c - 1), (self.r - 1, 0), (self.r - 1, self.c - 1)]
		dist = []
		i = 0
		for p in corners:
			dist.append((abs(end[0] - p[0]) + abs(end[1] - p[1]) , i))
			i += 1
		dest = corners[min(dist)[1]]
		(x1, y1) = end
		(x2, y2) = dest

		for i in range(x1 + 1, x2 + 1):
			l.append((i, y1))
		for i in range(x1 - 1, x2 - 1, -1):
			l.append((i, y1))

		x = l[len(l) - 1][0]		
		for i in range(y1 + 1, y2 + 1):
			l.append((x, i))
		for i in range(y1 - 1, y2 - 1, -1):
			l.append((x, i))	

		return l	

	
	def IFind(self, hval):
		startTime = time.time()
		nodesGen = 0
		maxSize = 0
		maxLen = 0
		mem = 0
		self.strategy.put(self.GetStartState())
		while not self.strategy.empty():
			node = self.strategy.get()
			maxSize = max(maxSize, sys.getsizeof(node))
			maxLen = max(maxLen, self.strategy.qsize())		
			if self.IsGoal(node):
				endTime = time.time()
				return [nodesGen, maxSize, maxLen, self.alter(node[2]), endTime - startTime, mem]
			for move in self.GetSuccessor(node, hval):
				nodesGen += 1
				self.strategy.put(move)
				mem += sys.getsizeof(move)		

		return None		
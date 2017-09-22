'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

from turtle import *
from collections import deque
from Queue import *

class tilefloor:
	'''
	Tile floor class
	'''
	TotalDirt = 0
	def __init__(self, size):
		self.n = size
		self.tile = []
		for i in range(0, size):
			temp = []
			for j in range(0, size):
				temp.append(0)
			self.tile.append(temp)

	def AddDirt(self , i , j):
		try:
			self.tile[i][j] = 1
			self.TotalDirt += 1
		except Exception as e:
			print (i , j)	

	def Clean(self, i, j):
		self.tile[i][j] = 0

	def IsDirty(self, i, j):
		if self.tile[i][j] == 1:
			return True
		else:
			return False				

	def IsFloorClean(self):
		for i in range(0, self.n):
			for j in range(0, self.n):
				if self.tile[i][j] == 1:
					return False;		
		return True
		
	def ShowFloor(self):
		for i in range(0, self.n):
			for j in range(0, self.n):
				print self.tile[i][j] ,	
			print ""

	def GetFloor(self):
		return self.tile


class Stack:
	'''
	LIFO stack
	'''
	def __init__(self):
		self.stack = []

	def pop(self):
		return self.stack.pop()

	def push(self, item):
		self.stack.append(item)

	def getsize(self):
		return len(self.stack)  

	def empty(self):
		return len(self.stack) == 0


class Queue:
	'''
	FIFO queue
	'''

	def __init__(self):
		self.queue = deque()
	  
	def push(self, item):
		self.queue.append(item)
	  
	def pop(self):
		return self.queue.popleft()

	def getsize(self):
		return len(self.queue)   
	  
	def empty(self):
		return len(self.queue) == 0	


def DrawSquare(s, c):
	'''
	Draws square of side s
	'''
	if(c == 1):
		pen(fillcolor = "brown", pensize = 2)
	else:
		pen(fillcolor = "white", pensize = 2)
	if c == 1:
		begin_fill()
	forward(s)
	right(90)
	forward(s)
	right(90)
	forward(s)
	right(90)
	forward(s)
	if c == 1:
		end_fill()


def DrawFloor(f):
	''' 
	Display floor configuration
	'''
	W  = '\033[0m'  # white (normal)
	R  = '\033[31m' # red
	G  = '\033[32m' # green
	O  = '\033[33m' # orange
	B  = '\033[34m' # blue
	P  = '\033[35m' # purple
	print
	for i in range(0, f.n):
		for j in range(0, f.n):
			if f.tile[i][j] == 1:
				print P + "D" + W,
			else:
				print "C",
		print 

	print P + "\nD - Dirty" + W	
	print "C - Clean"			
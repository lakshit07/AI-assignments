'''
Name : LAKSHIT BHUTANI
ID : 2014A7PS0095P
'''

from turtle import *
from utils import *
from dirtgenerator import *
from random import randint
from search import *

def initialize(f):	
	p = randint(1, 100)
	generator(f, p)

def DrawAnalysis(f, ans1, ans21, ans22):
	'''
	GUI part and corresponding calculations
	'''
	r1 = ans1[0]
	r2 = ans1[1]
	r3 = ans1[2]
	g1 = ans1[3]
	r4 = (len(g1) - 1)*2 + f.TotalDirt
	r5 = ans1[4]

	r61 = ans21[0]
	r62 = ans22[0]
	r71 = ans21[1]
	r72 = ans22[1]
	g21 = ans21[3]
	g22 = ans22[3]
	r81 = (len(g21) - 1)*2 + f.TotalDirt
	r82 = (len(g22) - 1)*2 + f.TotalDirt
	r91 = ans21[4]
	r92 = ans22[4]

	wn = Screen()
 	wn.title("Performance Analysis of T1 and T2 techniques")  

	# Draw center partition
	setup (width=1200, height=700, startx=0, starty=0)
	pu()
	goto(-200, 350)
	right(90)
	pd()
	forward(700)
	pu()	

	
	#T1 analysis
	goto(-570, 320)
	pd()
	write("T1 based analysis", font=("Arial", 14, "normal"))
	pu()
	goto(-590, 280)
	pd()
	write("Number of nodes generated : {}".format(r1) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, 250)
	pd()
	write("Memory allocated to one node : {} bytes".format(r2) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, 220)
	pd()
	write("Maximum growth of auxilary stack : {} ".format(r3) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, 190)
	pd()
	write("Total cost to clean room : {} ".format(r4) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, 160)
	pd()
	write("Total time to compute the path : {} milliseconds ".format(r5*1000) , font=("Arial", 10, "normal"))
	pu()

	# T2 analysis
	
	goto(-570, 100)
	pd()
	write("T2 based analysis", font=("Arial", 14, "normal"))
	pu()
	goto(-590, 60)
	pd()
	write("Number of nodes generated : h1 - {} and h2 - {}".format(r61, r62) , font=("Arial", 10, "normal"))
	pu()
	goto(-590,30)
	pd()
	write("Memory allocated to one node : h1 - {} and h2 - {} bytes".format(r71, r72) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, 0)
	pd()
	write("Total cost to clean room : h1 :- {} and h2 : {}".format(r81, r82) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, -30)
	pd()
	write("Total time to compute the path :- h1 : {} milliseconds ".format(r91*1000) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, -50)
	pd()
	write(" and h2 : {} milliseconds".format(r92*1000) , font=("Arial", 10, "normal"))
	pu()

	# Comparitive Analysis
	
	goto(-570, -110)
	write("Comparative analysis", font=("Arial", 14, "normal"))
	pu()
	goto(-590, -150)
	m1 = ans1[5]
	write("Memory used in T1 : {} bytes" . format(m1) , font=("Arial", 10, "normal"))
	pu()
	goto(-590, -180)
	m2 = (ans21[5] + ans22[5]) / 2
	write("Memory used in T2 (average): {} bytes" . format(m2) , font=("Arial", 10, "normal"))
	pu()


	# Run T1 and T2 for 10 random samples
	tt1 = 0
	tt2 = 0
	for i in range(0, 10):
		fl = tilefloor(f.n)
		initialize(fl)
		stack = Stack()
		us = USearch(fl, (0,0), stack)
		ans1 = us.UFind()
		tt1 += (len(ans1[3]) - 1)*2 + fl.TotalDirt
		pq = PriorityQueue()
		ins = ISearch(f, (0,0), pq)
		ans21 = ins.IFind(1) 
		tt2 += (len(ans21[3]) - 1)*2 + f.TotalDirt
		while not pq.empty():
			pq.get(False)
		ans22 = ins.IFind(2)
		tt2 += (len(ans22[3]) - 1)*2 + f.TotalDirt
	
	tt1 /= 10
	goto(-590, -210)
	pd()
	write("Average path cost for T1 : {}" . format(tt1) , font=("Arial", 10, "normal"))
	pu()
	tt2 /= 20
	goto(-590, -240)
	pd()
	write("Average path cost for T2 : {}" . format(tt2) , font=("Arial", 10, "normal"))
	pu()

	# Quadrant Boundaries
	goto(-200,0)
	pd()
	left(90)
	forward(800)
	pu()
	goto(200, -350)
	left(90)
	pd()
	forward(700)
	pu()

	# Draw G1
	X = -150
	Y = 325
	S = 300/f.n
	speed(0)

	right(90)
	goto(X + 150, Y + 5)
	write("T1 path", font=("Arial", 10, "italic"));
	goto(X, Y)
	pd()
	for i in range(0, f.n):
		for j in range(0, f.n):
			if f.IsDirty(i, j):
				DrawSquare(S, 1)
			else:
				DrawSquare(S, 0)
			right(90)
			forward(S)		
		pu()
		goto(xcor() - S*f.n, ycor() - S)
		pd()

	pen(fillcolor = "white", pencolor = "black", pensize = 2)
	pu()
	goto(-140, 310)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(120, 310)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(120, 35)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(-140, 35)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(X + S/2, Y - S/2)
	pen(fillcolor = "white", pencolor = "red", pensize = 5)
	pd()
	x = 0
	y = 0
	px = X + S/2
	py = Y - S/2
	speed(0)

	for i in g1:
		if i[0] != x:
			if i[0] > x:
				py -= S
			else:
				py += S
		elif i[1] != y:
			if i[1] > y:
				px += S
			else:
				px -= S
		else:
			pass

		x = i[0]
		y = i[1]
		goto(px, py)							


	# Draw G2
	pu()
	X = 250
	Y = 325
	S = 300/f.n
	speed(0)
	goto(X + 100, Y + 5)

	pd()
	pen(fillcolor = "white", pencolor = "black", pensize = 2)
	write("T2 path", font=("Arial", 10, "italic"));
	pu()
	
	goto(X, Y)
	pd()
	for i in range(0, f.n):
		for j in range(0, f.n):
			if f.IsDirty(i, j):
				DrawSquare(S, 1)
			else:
				DrawSquare(S, 0)
			right(90)
			forward(S)		
		pu()
		goto(xcor() - S*f.n, ycor() - S)
		pd()


	pen(fillcolor = "white", pencolor = "black", pensize = 2)
	pu()
	goto(260, 300)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(520, 300)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(520, 60)
	pd()
	write("Rest", font=("Arial", 8, "italic") )
	pu()
	goto(260, 60)
	pd()
	write("Rest", font=("Arial", 8, "italic") )

	pu()
	goto(X + S/2, Y - S/2 - 10)
	pen(fillcolor = "white", pencolor = "blue", pensize = 4)
	pd()
	x = 0
	y = 0
	px = X + S/2
	py = Y - S/2 - 10
	speed(5)

	for i in g21:
		if i[0] != x:
			if i[0] > x:
				py -= S
			else:
				py += S
		elif i[1] != y:
			if i[1] > y:
				px += S
			else:
				px -= S
		else:
			pass

		x = i[0]
		y = i[1]
		goto(px, py)

	pu()	
	goto(X + S/2, Y - S/2 + 10)
	pen(fillcolor = "white", pencolor = "green", pensize = 2)
	pd()
	x = 0
	y = 0
	px = X + S/2
	py = Y - S/2 + 10
	speed(5)

	for i in g22:
		if i[0] != x:
			if i[0] > x:
				py -= S
			else:
				py += S
		elif i[1] != y:
			if i[1] > y:
				px += S
			else:
				px -= S
		else:
			pass

		x = i[0]
		y = i[1]
		goto(px, py)	
	pu()	

	# G3 computation
	
	h1t = []
	h2t = []
	pen(fillcolor = "white", pencolor = "black", pensize = 1)

	for i in range(3, f.n + 1):
		fl = tilefloor(i)
		initialize(fl)
		pq = PriorityQueue()
		ins = ISearch(fl, (0,0), pq)
		ans21 = ins.IFind(1) 
		h1t.append(ans21[4]*1000)
		while not pq.empty():
			pq.get(False)
		ans22 = ins.IFind(2)
		h2t.append(ans22[4]*1000)

	goto(-150, -300)
	pd()
	forward(300)
	pu()
	backward(300)
	left(90)
	pd()
	forward(280)
	pu()
	backward(280)

	for i in range(3, 8):
		goto(-150 + (i-2)*50, -320)
		pd()
		write(str(i), font=("Arial", 10, "bold"));
		pu()

	goto(0, -340)
	pd()
	write("n", font=("Arial", 10, "bold"))	
	pu()

	maxi = max(h1t)
	maxi2 = max(h2t)
	maxi = int(max(maxi, maxi2))
	divs = 250.0 / maxi
	x = int(maxi / 10.0)

	for i in range(x, maxi + x, x):
		goto(-180, -300 + i*divs)
		pd()
		write(str(i), font=("Arial", 10, "bold"))
		pu()
			
	goto(-190, -190)
	pd()
	write("in ms", font=("Arial", 10, "normal"))	
	pu()	
	goto(-190, -180)
	pd()
	write("e", font=("Arial", 10, "normal"))	
	pu()
	goto(-190, -170)
	pd()
	write("m", font=("Arial", 10, "normal"))	
	pu()
	goto(-190, -160)
	pd()
	write("i", font=("Arial", 10, "normal"))	
	pu()
	goto(-190, -150)
	pd()
	write("t", font=("Arial", 10, "normal"))	
	pu()
	
	pen(pencolor = "blue", pensize = 2)
	for i in range(0, len(h1t)):
		goto(-150 + (i+1)*50, -300 + (h1t[i]*divs))
		if i == 0:
			pd()

	pu()		
	pen(pencolor = "green", pensize = 2)
	for i in range(0, len(h2t)):
		goto(-150 + (i+1)*50 + 5, -300 + (h2t[i]*divs) + 5)
		if i == 0:
			pd()
					
	pen(pencolor = "blue", pensize = 1)
	pu()
	goto(-20, -20);
	pd()
	right(90)
	forward(50)
	pu()
	forward(30)
	pd()
	write("Heuristic 1", font=("Arial", 10, "normal"))
	pu()

	pen(pencolor = "green", pensize = 1)
	pu()
	goto(-20, -50);
	pd()
	forward(50)
	pu()
	forward(30)
	pd()
	write("Heuristic 2", font=("Arial", 10, "normal"))
	pu()


	# G4 computations
 	pen(pencolor = "black", pensize = 1)

	t = []
	for i in range(10, 101, 5):
		fl = tilefloor(f.n)
		generator(fl, i)
		pq = PriorityQueue()
		ins = ISearch(fl, (0,0), pq)
		ans21 = ins.IFind(1)
		t.append(ans21[4] * 1000)
		# print str(i) + "%% done"

	goto(250, -300)
	pd()
	forward(300)
	pu()
	backward(300)
	left(90)
	pd()
	forward(280)
	pu()
	backward(280)

	for i in range(10, 101, 5):
		goto(250 + 15 * (i/5 - 1) , -330)
		pd()
		if i%10 == 0:
			write(str(i), font=("Arial", 10, "bold"));
		pu()

	goto(395, -340)
	pd()
	write("Dirt percentage" , font=("Arial", 8, "normal"))
	pu()

	maxi = max(t)
	tmax = int(ceil(maxi/250.0)*250)
	divs = tmax	/ 250

	for i in range(250, tmax, 250):
		goto(220, -300 + (i/divs))
		pd()
		write(str(i), font=("Arial", 10, "bold"))
		pu()

	goto(205, -125)
	pd()
	write("t" , font=("Arial", 8, "normal"))
	pu()
	goto(205, -135)
	pd()
	write("i" , font=("Arial", 8, "normal"))
	pu()
	goto(205, -145)
	pd()
	write("m" , font=("Arial", 8, "normal"))
	pu()
	goto(205, -155)
	pd()
	write("e" , font=("Arial", 8, "normal"))
	pu()
	goto(205, -165)
	pd()
	write("(ms)" , font=("Arial", 8, "normal"))
	pu()

	for i in range(0, len(t)):
		goto(250 + 15 * (i+1), -300 + t[i]/divs)
		if i == 0:
			pd()			
	
	exitonclick()	
	

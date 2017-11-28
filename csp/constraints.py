from preprocess import *
from math import *

# course number c , type of class t (L,T,P), and number of class k (L1, L2, L3, etc)
# being assigned day d, slot s, and lecture hall [1..5] or lab [6..10] r

def c1(c, t, k, d, s, r):
	if course[c][2] > 0:
		if t == 2:
			if s < 5 or r < 6:
				return False
			else:
				return True	
		else:
			return True	
	else:
		return True	

def c2(c, t, k, d, s, r):
	if course[c][2] > 0:
		if t == 2:
			n = course[c][2]
			assign[c][t][k] = (d, s, r)
			for i in range(1, n):
				if (assign[c][t][i-1] != -1) and (assign[c][t][i] != -1) and ((assign[c][t][i-1][0] != assign[c][t][i]) or (assign[c][t][i-1][1] != assign[c][t][i][1] - 1)):
					assign[c][t][k] = -1
					return False
			assign[c][t][k] = -1
			return True			
		else:
			return True	
	else:
		return True

def c3(c, t, k, d, s, r):
	if course[c][0] == 0 or course[c][1] == 0:
		return True
	else:
		assign[c][t][k] = (d, s, r)
		help1 = []
		help2 = []
		for i in range(0, course[c][0]):
			if assign[c][0][i] != -1:
				help1.append(assign[c][0][i][0]) 
		for i in range(0, course[c][1]):
			if assign[c][1][i] != -1:
				help2.append(assign[c][1][i][0])

		assign[c][t][k] = -1
		t1 = set(help1)
		t2 = set(help2)
		t3 = t1.intersection(t2)

		if len(t3) > 0:
			return False
		else:
			return True

def c4(c, t, k, d, s, r):
	assign[c][t][k] = (d, s, r)
	if c in proga_dc:
		for j in proga_dc:
			if j == c:
				continue
			else:
				help = []
				for i in assign[c][0]:
					if i != -1:
						help.append((i[0] , i[1]))

				for i in assign[c][1]:
					if i != -1:
						help.append((i[0] , i[1]))

				for i in assign[c][2]:
					if i != -1:
						help.append((i[0] , i[1]))

				if (d, s) in help:
					assign[c][t][k] = -1
					return False
									
	if c in progb_dc:
		for j in progb_dc:
			if j == c:
				continue
			else:
				help = []
				for i in assign[c][0]:
					if i != -1:
						help.append((i[0] , i[1]))

				for i in assign[c][1]:
					if i != -1:
						help.append((i[0] , i[1]))

				for i in assign[c][2]:
					if i != -1:
						help.append((i[0] , i[1]))

				if (d, s) in help:
					assign[c][t][k] = -1
					return False

	if c in progc_dc:
		for j in progc_dc:
			if j == c:
				continue
			else:
				help = []
				for i in assign[c][0]:
					if i != -1:
						help.append((i[0] , i[1]))

				for i in assign[c][1]:
					if i != -1:
						help.append((i[0] , i[1]))

				for i in assign[c][2]:
					if i != -1:
						help.append((i[0] , i[1]))

				if (d, s) in help:
					return False
	return True		

def c5(c, t, l, d, s, r):
	ge = list(set(proga_ge) | set(progb_ge) | set(progc_ge))
	if c not in ge:
		return True
	else:
		assign[c][t][l] = (d, s, r)	
		for i in ge:
			for j in ge:
				if i == j:
					continue
				else:	
					help1 = []
					help2 = []
					for k in assign[i][0]:
						if k == -1:
							continue
						else:
							help1.append(k[0])

					for k in assign[i][1]:
						if k == -1:
							continue
						else:
							help1.append(k[0])

					for k in assign[i][2]:
						if k == -1:
							continue
						else:
							help1.append(k[0])

					for k in assign[j][0]:
						if k == -1:
							continue
						else:
							help2.append(k[0])

					for k in assign[j][1]:
						if k == -1:
							continue
						else:
							help2.append(k[0])

					for k in assign[j][2]:
						if k == -1:
							continue
						else:
							help2.append(k[0])

					t1 = set(help1)
					t2 = set(help2)
					t3 = t1.intersection(t2)
					assign[c][t][l] = -1

					if len(t3) > 0:
						return False
					else:
						return True									


def c6(c, t, k, d, s, r):
	if course[c][0] == 0 or t != 0:
		return True
	else:
		help = []
		for i in assign[c][0]:
			help.append(i)
		if d in help:
			return False
		else:
			return True

def c8(c, t, k, d, s, r):
	if c in prof[4]:
		if d == 4:
			return False
	
	if c in prof[1]:
		if 1 <= s and s <= 3:
			return True
		else:
			return False

	return True

def c9(c, t, k, d, s, r):
	if course[c][0] == 0:
		return True
	for i in range(1, len(prof)):
		if c in prof[i]:
			for j in prof[i]:
				if j == c:
					continue
				else:
					help = []
					for k in assign[j][0]:
						if k != -1 and k[0] == d:
							help.append(k[1])
					for k in help:
						if abs(k - s) <= 1:
							return False
	return True


def c11(c, t, k, d, s, r):
	for i in range(1, len(prof)):
		for j in prof[i]:
			help = []
			for k in assign[j][0]:
				if k != -1:
					help.append((k[0], k[1], k[2]))
			for k in assign[j][1]:
				if k != -1:
					help.append((k[0], k[1], k[2]))
			for k in assign[j][2]:
				if k != -1:
					help.append((k[0], k[1], k[2]))
			t1 = set(help)
			if len(t1) != len(help):
				return False
	return True
	

def c10(c, t, k, d, s, r):
	for i in pka:
		if c in i:
			for j in i:
				if j == i:
					continue
				else:
					help = []
					for k in assign[j][0]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					for k in assign[j][1]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					for k in assign[j][2]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					if (d, s, r) in help:
						return False
	for i in pkb:
		if c in i:
			for j in i:
				if j == i:
					continue
				else:
					help = []
					for k in assign[j][0]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					for k in assign[j][1]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					for k in assign[j][2]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					if (d, s, r) in help:
						return False
	for i in pkc:
		if c in i:
			for j in i:
				if j == i:
					continue
				else:
					help = []
					for k in assign[j][0]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					for k in assign[j][1]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					for k in assign[j][2]:
						if k != -1:
							help.append((k[0], k[1], k[2]))
					if (d, s, r) in help:
						return False

	return True
	

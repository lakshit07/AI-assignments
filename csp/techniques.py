from constraints import *
from preprocess import *
taken = {}

def DFS_BT():
	for c in range(1, len(course)):
		if course[c][0] > 0:
			for k in range(0, course[c][0]):
				for d in range(1, 7):
					if d < 6:
						for s in range(1, 8):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 0, k, d, s, r) and c2(c, 0, k, d, s, r) and c3(c, 0, k, d, s, r) and c4(c, 0, k, d, s, r) and c5(c, 0, k, d, s, r) and c6(c, 0, k, d, s, r) and c8(c, 0, k, d, s, r) and c9(c, 0, k, d, s, r) and c10(c, 0, k, d, s, r) and c11(c, 0, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 0, k)
					else:
						for s in range(1, 5):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 0, k, d, s, r) and c2(c, 0, k, d, s, r) and c3(c, 0, k, d, s, r) and c4(c, 0, k, d, s, r) and c5(c, 0, k, d, s, r) and c6(c, 0, k, d, s, r) and c8(c, 0, k, d, s, r) and c9(c, 0, k, d, s, r) and c10(c, 0, k, d, s, r) and c11(c, 0, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 0, k)
		if course[c][1] > 0:
			for k in range(0, course[c][1]):
				for d in range(1, 7):
					if d < 6:
						for s in range(1, 8):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 1, k, d, s, r) and c2(c, 1, k, d, s, r) and c3(c, 1, k, d, s, r) and c4(c, 1, k, d, s, r) and c5(c, 1, k, d, s, r) and c6(c, 1, k, d, s, r) and c8(c, 1, k, d, s, r) and c9(c, 1, k, d, s, r) and c10(c, 1, k, d, s, r) and c11(c, 1, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)
					else:
						for s in range(1, 5):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 1, k, d, s, r) and c2(c, 1, k, d, s, r) and c3(c, 1, k, d, s, r) and c4(c, 1, k, d, s, r) and c5(c, 1, k, d, s, r) and c6(c, 1, k, d, s, r) and c8(c, 1, k, d, s, r) and c9(c, 1, k, d, s, r) and c10(c, 1, k, d, s, r) and c11(c, 1, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)
		
		if course[c][2] > 0:
			for k in range(0, course[c][2]):
				for d in range(1, 7):
					if d < 6:
						for s in range(1, 8):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 2, k, d, s, r) and c2(c, 2, k, d, s, r) and c3(c, 2, k, d, s, r) and c4(c, 2, k, d, s, r) and c5(c, 2, k, d, s, r) and c6(c, 2, k, d, s, r) and c8(c, 2, k, d, s, r) and c9(c, 2, k, d, s, r) and c10(c, 2, k, d, s, r) and c11(c, 2, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)
					else:
						for s in range(1, 5):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 2, k, d, s, r) and c2(c, 2, k, d, s, r) and c3(c, 2, k, d, s, r) and c4(c, 2, k, d, s, r) and c5(c, 2, k, d, s, r) and c6(c, 2, k, d, s, r) and c8(c, 2, k, d, s, r) and c9(c, 2, k, d, s, r) and c10(c, 2, k, d, s, r) and c11(c, 2, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)

	if len(taken) == 0:
		print "No schedule possible"
	else:
		print taken


def DFS_BT_Constraint_Propagation():
	for c in range(1, len(course)):
		if course[c][0] > 0:
			for k in range(0, course[c][0]):
				for d in range(1, 7):
					if d < 6:
						for s in range(1, 8):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 0, k, d, s, r) and c2(c, 0, k, d, s, r) and c3(c, 0, k, d, s, r) and c4(c, 0, k, d, s, r) and c5(c, 0, k, d, s, r) and c6(c, 0, k, d, s, r) and c8(c, 0, k, d, s, r) and c9(c, 0, k, d, s, r) and c10(c, 0, k, d, s, r) and c11(c, 0, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 0, k)
					else:
						for s in range(1, 5):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 0, k, d, s, r) and c2(c, 0, k, d, s, r) and c3(c, 0, k, d, s, r) and c4(c, 0, k, d, s, r) and c5(c, 0, k, d, s, r) and c6(c, 0, k, d, s, r) and c8(c, 0, k, d, s, r) and c9(c, 0, k, d, s, r) and c10(c, 0, k, d, s, r) and c11(c, 0, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 0, k)
		if course[c][1] > 0:
			for k in range(0, course[c][1]):
				for d in range(1, 7):
					if d < 6:
						for s in range(1, 8):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 1, k, d, s, r) and c2(c, 1, k, d, s, r) and c3(c, 1, k, d, s, r) and c4(c, 1, k, d, s, r) and c5(c, 1, k, d, s, r) and c6(c, 1, k, d, s, r) and c8(c, 1, k, d, s, r) and c9(c, 1, k, d, s, r) and c10(c, 1, k, d, s, r) and c11(c, 1, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)
					else:
						for s in range(1, 5):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 1, k, d, s, r) and c2(c, 1, k, d, s, r) and c3(c, 1, k, d, s, r) and c4(c, 1, k, d, s, r) and c5(c, 1, k, d, s, r) and c6(c, 1, k, d, s, r) and c8(c, 1, k, d, s, r) and c9(c, 1, k, d, s, r) and c10(c, 1, k, d, s, r) and c11(c, 1, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)
		
		if course[c][2] > 0:
			for k in range(0, course[c][2]):
				for d in range(1, 7):
					if d < 6:
						for s in range(1, 8):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 2, k, d, s, r) and c2(c, 2, k, d, s, r) and c3(c, 2, k, d, s, r) and c4(c, 2, k, d, s, r) and c5(c, 2, k, d, s, r) and c6(c, 2, k, d, s, r) and c8(c, 2, k, d, s, r) and c9(c, 2, k, d, s, r) and c10(c, 2, k, d, s, r) and c11(c, 2, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)
					else:
						for s in range(1, 5):
							for r in range(1, 6):
								if (d, s, r) not in taken.keys() and c1(c, 2, k, d, s, r) and c2(c, 2, k, d, s, r) and c3(c, 2, k, d, s, r) and c4(c, 2, k, d, s, r) and c5(c, 2, k, d, s, r) and c6(c, 2, k, d, s, r) and c8(c, 2, k, d, s, r) and c9(c, 2, k, d, s, r) and c10(c, 2, k, d, s, r) and c11(c, 2, k, d, s, r):
									assign[c][0][k] = (d, s, r)
									taken[d, s, r] = (c, 1, k)

	if len(taken) == 0:
		print "No schedule possible"
	else:
		print taken	


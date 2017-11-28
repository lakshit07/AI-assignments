import csv
proga = []
proga_dc = []
proga_ge = []
proga_de = []
progb = []
progb_dc = []
progb_ge = []
progb_de = []
progc = []
progc_dc = []
progc_ge = []
progc_de = []
course = []
prof = []
pkga = []
pkgb = []
pkgc = []
assign = [[]]
pka = []
pkb = []
pkc = []

def type(t):
	if t == "DC":
		return 1
	elif t == "DE":
		return 2
	elif t == "GE":
		return 3
	else:
		return -1
				
def generate_packages(tfile):
	course.append((0, 0, 0))
	prof.append(())
	
	fil = open(tfile, 'r')
	text = csv.reader(fil, delimiter = ',')
	c = False
	p = False
	i = 0
	for line in text:
		if line[0] == "$COURSES$":
			continue
		elif line[0] == "Courses":
			c = True
			continue	
		elif line[0] == "$PROF$":
			continue
		elif line[0] == "Professor":
			c = False
			p = True
			i = 0
			continue	
		elif c:
			i += 1
			if type(line[1]) == 1:
				proga.append((i, 1))
				proga_dc.append(i)
			elif type(line[1]) == 2:
				proga.append((i, 2))
				proga_de.append(i)
			elif type(line[1]) == 3:
				proga.append((i, 3))
				proga_ge.append(i)

			if type(line[2]) == 1:
				progb.append((i, 1))
				progb_dc.append(i)
			elif type(line[2]) == 2:
				progb.append((i, 2))
				progb_de.append(i)
			elif type(line[2]) == 3:
				progb.append((i, 3))
				progb_ge.append(i)

			if type(line[3]) == 1:
				progc.append((i, 1))
				progc_dc.append(i)
			elif type(line[3]) == 2:
				progc.append((i, 2))
				progc_de.append(i)
			elif type(line[3]) == 3:
				progc.append((i, 3))
				progc_ge.append(i)

			x = line[4].split()	
			course.append((int(x[0]) , int(x[1]) , int(x[2])))
		elif p:
			i += 1
			temp = []
			for j in line:
				if j[0] == 'P':
					continue
				elif j[0] == 'N':
					break
				else:
					temp.append(int(j[2:]))
			prof.append(tuple(temp))

	print "Package for Program A"
	for a in range(0, len(proga_dc) - 2):
		for b in range(a+1, len(proga_dc) - 1):
			for c in range(b+1, len(proga_dc)):
				for d in range(0, len(proga_de) - 1):
					for e in range(d+1, len(proga_de)):
						for f in range(0, len(proga_ge)):
							s = "DC : C_%02d C_%02d C_%02d | DE : C_%02d C_%02d | GE : C_%02d" % (proga_dc[a], proga_dc[b], proga_dc[c], proga_de[d], proga_de[e], proga_ge[f])
							pkga.append(s)
							pka.append((proga_dc[a], proga_dc[b], proga_dc[c], proga_de[d], proga_de[e], proga_ge[f]))
							print s
	print ""						
	print "Package for Program B"
	for a in range(0, len(progb_dc) - 2):
		for b in range(a+1, len(progb_dc) - 1):
			for c in range(b+1, len(progb_dc)):
				for d in range(0, len(progb_de) - 1):
					for e in range(d+1, len(progb_de)):
						for f in range(0, len(progb_ge)):
							s = "DC : C_%02d C_%02d C_%02d | DE : C_%02d C_%02d | GE : C_%02d" % (progb_dc[a], progb_dc[b], progb_dc[c], progb_de[d], progb_de[e], progb_ge[f])
							pkgb.append(s)
							pkb.append((progb_dc[a], progb_dc[b], progb_dc[c], progb_de[d], progb_de[e], progb_ge[f]))
							print s

	print ""				
	print "Package for Program C"
	for a in range(0, len(progc_dc) - 2):
		for b in range(a+1, len(progc_dc) - 1):
			for c in range(b+1, len(progc_dc)):
				for d in range(0, len(progc_de) - 1):
					for e in range(d+1, len(progc_de)):
						for f in range(0, len(progc_ge)):
							s = "DC : C_%02d C_%02d C_%02d | DE : C_%02d C_%02d | GE : C_%02d" % (progc_dc[a], progc_dc[b], progc_dc[c], progc_de[d], progc_de[e], progc_ge[f])						
							pkgc.append(s)
							pkc.append((progc_dc[a], progc_dc[b], progc_dc[c], progc_de[d], progc_de[e], progc_ge[f]))
							print s

	print ""
	print "Package for Professors"
	for i in range(1, len(prof)):
		print ("Prof-%d : " % i),
		for j in prof[i]:
			print("C_%02d " % j),
		print ""

	for i in range(1, len(course)):
		l = course[i][0]
		t = course[i][1]
		p = course[i][2]
		temp = [[], [], []]
		for j in range(0, l):
			temp[0].append(-1)
		for j in range(0, t):
			temp[1].append(-1)
		for j in range(0, p):
			temp[2].append(-1)
		assign.append(temp)					


def Constraint_Graph():
	print "\nNodes in the constraint graph represent courses which have variables L1, L2,..., Ln where n is number of lectures, T1, T2,..., Tm where m are the number of tutorials and P1, P2,..., Pk where k are the number of laboratory practicals"
	print "\nThe domain of each variable is tuple (d, s, c) where d is the day [1..7], s is the slot on the day[1..7] and c is either lecture hall number[1..5] or laboratory number [6..10]"
	
	print "\nConstraint - 1 : Labs in AN"
	print "Allowed combinations. ['X' is don't care]"
	for i in range(1, len(course)):
		if course[i][2] > 0:
			print ("C_%02d : P - ( X, X, [5,6,7] )" % i)

	print "\nConstraint - 2: Labs are consecutive"
	print "Allowed combinations. ['X' is don't care, 'Y' is any variable]"
	for i in range(1, len(course)):
		if course[i][2] > 0:
			print ("C_%02d : P - " % i),
			for j in range(0, course[i][2]):
				if j == 0:
					print "( X, X, Y) ",
				else:
					print "( X, X, Y + %d)" % j,	
			print ""

	print "\nConstraint - 3: Lectures and Tutorial not on same day"
	print "Allowed combinations. ['X' is don't care, 'Y', 'Z' is variables which are unequal]"						
	for i in range(1, len(course)):
		if course[i][0] > 0 and course[i][1] > 0:
			print ("C_%02d : L - (Y, X, X) T - (Z, X, X)" % i)

	print "\nConstraint - 4: No two DC for a program together"
	print "These courses can't be of the form (Y, X, X) and (Y + 1, X, X) where 'X' is don't care and 'Y' is a variable"						
	
	if len(proga_dc) > 1:
		print "Program A"
		for i in proga_dc:
			print "C_%02d " % i,
		print ""

	if len(progb_dc) > 1:	
		print "Program B"
		for i in progb_dc:
			print "C_%02d " % i,
		print ""

	if len(progc_dc) > 1:	
		print "Program C"
		for i in progc_dc:
			print "C_%02d " % i,
		print ""

	print "\nConstriant - 5: GE courses not on the same day"
	print "These courses can't be of the form (Y, X, X)"
	temp = list(set(proga_ge) | set(progb_ge) | set(progc_ge))
	for i in temp:
		print "C_%02d" % i ,
	print ""
	
	print "\nConstriant - 6: Atmost one lecture of a course on a day"
	print "The L's of these courses can't be of the form (Y, X, X)"
	help = []
	for i in range(1, len(course)):
		if course[i][0] > 0:
			help.append(i)
	temp = list(set(help))
	for i in temp:
		print "C_%02d" % i ,
	print ""

	print "\nConstriant - 7: Two laboratory sessions for practical courses"
	print "These courses will have P1, P2, ... , P2*k variables where k is the number of laboratory sessions"
	help = []
	for i in range(1, len(course)):
		if course[i][2] > 0:
			help.append(i)
	temp = list(set(help))
	for i in temp:
		print "C_%02d" % i ,
	print ""

	print "\nConstraint - 8: Prof-4 not on Thursday and Prof-1 during {1,2,3} slots only"
	print "These courses will be of the form (4, X, X)"
	for i in prof[4]:
		print "C_%02d" % i,
	print ""
	print "These courses will be of the form (X, [1,2,3], X)"
	for i in prof[1]:
		print "C_%02d" % i,
	print ""

	print "\nConstraint - 9: Lectures of professors should not be in succession"
	print "These courses can't be of the form (Y, X, X) and (Y + 1, X, X)"
	for i in range(1, len(prof)):
		if len(prof[i]) > 1:
			for j in prof[i]:
				print "C_%02d" % j,
			print ""

	print "\nConstraint - 10: No clash in any student package"
	print "No two of these courses in a line can be of the form (Y, Z, X) - Package for program A"
	for i in pkga:
		print i
	print "\nNo two courses can be of the form (Y, Z, X) - Package for program B"
	for i in pkgb:
		print i
	print "\nNo two courses can be of the form (Y, Z, X) - Package for program C"
	for i in pkgc:
		print i

	print "\nConstraint - 11: No clash in professor package"
	print "No two of these courses in a line can be of the form (Y, Z, X)"
	for i in range(1, len(prof)):
		if len(prof[i]) > 1:
			for j in prof[i]:
				print("C_%02d " % j),
			print ""					
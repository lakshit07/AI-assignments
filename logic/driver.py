from cnf import *

def kb_to_cnf():
	r = ['rules1.txt', 'rules2.txt', 'rules3.txt', 'rules4.txt']
	w = ['kb1.txt', 'kb2.txt', 'kb3.txt', 'kb4.txt']

	for i in range(0, 4):
		rd = open(r[i], 'r')
		wr = open(w[i], 'w')
		line = rd.readline()
		while line:
			st = parse_string(line)
			wr.write(infix(cnf(st)) + "\n")
			line = rd.readline()
		print w[i] + " generated"	
		rd.close()
		wr.close()

def main():
	while True:
		print "\nOption 1: Convert KB to CNF\n" , "Option 2: Execute queries\n" , "Option 3: GUI\n" , "Option 4: Quit\n"
		print "Enter choice : ",
		ch = int(input())

		if ch == 1:
			kb_to_cnf()
		elif ch == 2:
			print "Not implemented"
		elif ch == 3:
			print "Not Implemented"
		else:
			break			

          
if __name__ == "__main__":
    main()

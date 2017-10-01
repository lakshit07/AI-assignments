from utils import *
from game import *
import sys

def main():
	b = tictactoe()
	r[2] = sys.getsizeof(b)
	while True:
		print "\nOption 1: Display the empty board\n" , "Option 2: Play the game using Minimax algorithm\n" , "Option 3: Play the game using Alpha Beta pruning\n" , "Option 4: Show all results R1-R12\nOption 5: Quit\n"
		print "Enter choice : ",
		ch = int(input())
		if ch == 1:
			b.display()
		elif ch == 2:
			reset()
			b.display()
			b.bestmove()
			onscreenclick(findmark)
			while True:
				firstmove(0)
				print "Do you want to quit (Y/N) [Enter after playing the game] ?",
				z = raw_input()
				reset()
				if z.lower() == 'y':
					break
				else:
					b.display()
					onscreenclick(findmark)
					firstmove(0)
		elif ch == 3:
			b.display()
			b.bestmoveab()
			onscreenclick(findmarkab)
			while True:
				firstmove(1)
				print "Do you want to quit (Y/N) [Enter after playing the game] ?",
				z = raw_input()
				if z.lower() == 'y':
					break
				else:
					reset()
					b.display()
					onscreenclick(findmarkab)
					firstmove(1)
		elif ch == 4:
			analysis()							
		elif ch == 5:
			break	


if __name__ == "__main__":
    main()	

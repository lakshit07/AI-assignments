from preprocess import *
from constraints import *
from techniques import *

def main():
	'''
	Driver function with various options
	'''
	fil = str(raw_input("Enter the data csv file : "))
	#fil = "data.csv"
	while True:
		print "\nOption 1: Display the packages\n", "Option 2: Display the constraint graph appropriately\n","Option 3: Execute DFS+BT with and without the heuristic\n", "Option 4: Execute DFS+BT+Constraint_Propagation with and without the heuristic\nOption 5: Quit"
		ch = int(input())

		if ch == 1:
			generate_packages(fil)
		elif ch == 2:
			Constraint_Graph()
		elif ch == 3:
			DFS_BT()
		elif ch == 4:			
			DFS_BT_Constraint_Propagation()
		else:
			break		

if __name__ == "__main__":
    main()	
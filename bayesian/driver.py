'''
NAME : Lakshit Bhutani
ID : 2014A&PS0095P
'''
import os

from graph import *
from blanket import *
from query import *
from gui import *

'''
Main driver code
'''
def main():
    print "Enter input file : ",
    fname = raw_input()
    #fname = "input1.txt"
    createBayesian(fname)

    while True:
        print "\n1. Print Markov's Blanket of a variable\n2. GUI\n3. Quit"
        print "Enter choice : ",
        ch = int(input())
        if ch == 1:
            print "Enter the variable : ",
            v = raw_input()
            bl = markovBlanket(v)
            for i in bl:
                print i,
            print 
        elif ch == 2:
            graphics()
        else:
            break        

if __name__ == "__main__":
    main()	   

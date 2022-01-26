import math
import sys
import stdio

#Pert
#A is the amount of money you have to work with

A = int(sys.argv[1])

#R is the interest rate
R = float(sys.argv[2])
#P = principle
Y = float(sys.argv[3])
#Y = Years or whatever, time, you get the idea
#0.5 is still valid input
P = (A * math.exp(R) * Y)

stdio.writeln(P)

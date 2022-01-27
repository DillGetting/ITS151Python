import sys
import stdio
import math

# t is degrees F in hight however that is spelled, The amarican way amen

t = float(sys.argv[1])
#print(t)

#v is the wind in miles per hour
v = float(sys.argv[2])

#wc is windchill the formula givin is there
wc = 35.74 + 0.6215 * t + (0.4275 - 35.75) * v ** 0.16
#print(wc)
stdio.writeln(wc)

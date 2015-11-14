#calculate T_c, mean over all numerical values
from numpy import *

L = [20,40,60,80]

#read from plots:
T_c1 = [2.32, 2.29, 2.28, 2.27] #C_v
T_c2 = [2.34, 2.31, 2.3, 2.3] #chi

x1 = zeros(len(T_c1)-1)
x2 = zeros(len(T_c1)-1)

for i in range(len(T_c1)-1):
	x1[i] = (T_c1[i]*L[i] - T_c1[i+1]*L[i+1])/(L[i] - L[i+1])
	x2[i] = (T_c2[i]*L[i] - T_c2[i+1]*L[i+1])/(L[i] - L[i+1])

print "Numerical T_c = ", (mean(x1) + mean(x2))/2

theory = 2.269

print "Theoretical T_c = ", theory

print "Error in estimate = ", abs((mean(x1) + mean(x2))/2 - theory)
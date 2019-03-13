import numpy as np
import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import sys
from decimal import *
import scipy.optimize
def problem_5():
	# User defined precision for implementing the Decimal()
	getcontext().prec = 16
	e_val = 0.0 # Initial value 
	r = 10.0
	i = 0
	while True:
		e_new = (1.0+1.0/(r**i))**(r**i)
		print(r'%.1E & %.13E' %(r**i,e_new))
		if (np.abs(e_val-e_new) < 1.0e-13):
			print('We are stopping at %.1E step, the value computed is %.13E' %(r**i, e_new))
			break
		else:
			e_val = e_new
			i+=1
	# Print the value of exponent computed by the python numpy library
	print(np.exp(1))
	return 0

def main():
	problem_5()

if __name__ == '__main__':
	main()
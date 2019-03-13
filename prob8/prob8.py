# Global imports
import numpy as np
import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import sys
from decimal import *
import scipy.optimize
# Local imports
from scipy import integrate


def problem_8():
	# The kth y value to obtain
	k = 20

	# Solving part c
	eps = 1.0e-15 # The machine epsilon

	# Find the correct N
	N_factorial = math.factorial(k)/eps

	# Find the nearest integer
	# NOTE: Crude approach
	i = 0 # counter
	while True:
		if(math.factorial(k+i) > N_factorial):
			N = k+i
			print('The estimated value of N is %d' %(N))
			break
		else:
			i+=1
	# Solving part d
	# Starting the reverse recursion at N
	# Initial guess at N
	y_guess = 0.0
	for i in range(N,k,-1):
		y_compute = (np.exp(1.0) - y_guess)/i
		y_guess = y_compute
	# Print the computed value
	print('The computed value of y_20 is %.15f' %(y_compute))
	# Compute the true integral
	f = lambda x : np.exp(x)*(x**k)
	y_true = integrate.quad(f, 0.0, 1.0)
	# Print the true value
	print('The true value of y_20 is %.15f' %(y_true[0]))

def main():
	problem_8()

if __name__ == '__main__':
	main()
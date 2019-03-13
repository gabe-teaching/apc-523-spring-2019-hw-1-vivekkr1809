import numpy as np
import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import sys
from decimal import *
import scipy.optimize

def problem_7():
	x = sp.Symbol('x')
	roots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	eqn = 1
	for i in roots:
		eqn *=(x-i)

	p = sp.poly(eqn, x)
	# Print the polynomial and the coefficients
	# print(p)
	# print(p.all_coeffs())
	# Save the coefficients as integers for later manipulation
	coeff_int = p.all_coeffs()
	# Save the coefficients as floats
	coefficients = np.array(coeff_int, dtype=np.float64)
	coefficients = np.flip(coefficients)
	coefficients[19] -= 2.0**(-23)
	print(coefficients)
	# Evaluate the the polynomial at a given x
	f = lambda x: np.polynomial.polynomial.polyval(x, coefficients)
	# Evaluate the derivative of the polynomial at x
	coefficients_derivative = np.polynomial.polynomial.polyder(coefficients)
	f_prime = lambda x: np.polynomial.polynomial.polyval(x, coefficients_derivative)
	# Evaluate the roots based on initial guess
	print(scipy.optimize.root_scalar(f, method='newton', fprime= f_prime, x0=21, maxiter=1000))

	# Evaluate the roots using builtin function
	print(np.polynomial.polynomial.polyroots(coefficients))	

def main():
	problem_7()

if __name__ == '__main__':
	main()
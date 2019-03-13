import numpy as np
import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import sys
from decimal import *
import scipy.optimize

def problem_6():
	n_elements = 1001
	x = np.linspace(0.0, 10.0, num=n_elements, endpoint=True)
	sqrt_x = x
	n_times = 52
	i = 0
	while(i<n_times):
		sqrt_x = np.sqrt(sqrt_x)
		i+=1
	sqr_sqrt_x = sqrt_x
	j = 0
	while(j<n_times):
		sqr_sqrt_x = np.square(sqr_sqrt_x)
		j+=1

	# Plot the results
	plt.plot(x, sqr_sqrt_x)
	plt.title('Squared value vs True Value for n=%d' %(n_times))
	plt.xlabel('x')
	plt.ylabel('Squared value')
	plt.plot(x,x,'-')
	plt.savefig('plot_for_n_52'+'.pdf',bbox_inches='tight', format='pdf', dpi=1000)
	plt.show()
	return 0

def main():
	problem_6()

if __name__ == '__main__':
	main()
"""
This is the accompanyng code for HW 1 for APC 523 along with the includes
Author(s): Vivek Kumar
Last Updated: 13th March 2019
"""
import numpy as np
import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import sys
from decimal import *
import scipy.optimize
# Import the solutions
from prob2.prob2 import problem_2
from prob8.prob8 import problem_8

def main():
	print('#################')
	print('Solving Problem 2')
	problem_2()
	print('\n')
	print('#################')
	print('Solving Problem 7')
	print('\n')
	print('#################')
	print('Solving Problem 8')
	problem_8()


if __name__ == '__main__':
	main()
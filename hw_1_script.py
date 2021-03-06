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
from prob5.prob5 import problem_5
from prob6.prob6 import problem_6
from prob7.prob7 import problem_7
from prob8.prob8 import problem_8

def main():
	print('#################')
	print('Solving Problem 2')
	problem_2()
	print('\n')
	print('#################')
	print('Solving Problem 5')
	problem_5()
	print('\n')
	print('#################')
	print('Solving Problem 6')
	problem_6()
	print('\n')
	print('#################')
	print('Solving Problem 7')
	problem_7()
	print('\n')
	print('#################')
	print('Solving Problem 8')
	problem_8()


if __name__ == '__main__':
	main()
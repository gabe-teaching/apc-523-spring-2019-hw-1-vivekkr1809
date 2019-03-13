# Global imports
import numpy as np
import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import sys
from decimal import *
import scipy.optimize

def rounding(x,sig=5):
	return round(x, sig-int(math.floor(math.log10(abs(x))))-1)

def problem_2_positive():
	print('Solving for exp(5.5)')
	# Power of exponent
	x = 5.5
	# Compute the value and print at each step
	n_max = 30
	# Initialize the numerator and denominator
	prev_num = 1.0
	prev_den = 1.0
	exp_value_left = 0.0
	exp_value_right = 0.0
	# Create an empty list
	term_list =[1.0]

	# Loop over to compute each term and value of exp(5.5)
	for i in range(1, n_max+1):
		num = rounding(prev_num*x)
		prev_num = num
		den = rounding(prev_den*i)
		prev_den = den
		term = rounding(num/den)
		term_list.append(term)
	# Convert list to numpy array
	term_list = np.asarray(term_list)
	l_term_list = len(term_list)
	# Add from left to right
	for t in range(l_term_list):
		exp_value_left = rounding(exp_value_left+term_list[t])
		
	print('The value of exp(5.5) computed left to right is %.5E' %(exp_value_left))

	# Add from right to left
	for t in range(l_term_list):
		exp_value_right = rounding(exp_value_right+term_list[n_max-t-1])
		
	print('The value of exp(5.5) computed right to left is %.5E' %(exp_value_right))
		# print('The value of num is %f, den is %f, term is %f' %(num, den, term))
		# exp_value = rounding(exp_value+term)
		# print(r'%d & %.5E & %.5E & %.5E & %.5E \\' %(i, num, den, term, exp_value))

	print('True value of exp(5.5) is %f' %(np.exp(5.5)))
	print('The relative error is left-to-right %.6f' %(abs(np.exp(5.5)-exp_value_left)/np.exp(5.5)))
	print('The relative error is right-to-left %.6f' %(abs(np.exp(5.5)-exp_value_right)/np.exp(5.5)))

	print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
	return 0

def problem_2_negative():
	print('Solving for exp(-5.5)')
	# Power of exponent
	x = 5.5
	# Compute the value and print at each step
	n_max = 30
	# Initialize the numerator and denominator
	prev_num = 1.0
	prev_den = 1.0
	exp_value_left = 0.0
	exp_value_right = 0.0
	# Create an empty list
	term_list =[1.0]

	# Loop over to compute each term and value of exp(5.5)
	for i in range(1, n_max+1):
		num = rounding(prev_num*x)
		prev_num = num
		den = rounding(prev_den*i)
		prev_den = den
		term = rounding(num/den)
		term_list.append(term)
	# Convert list to numpy array
	term_list = np.asarray(term_list)
	l_term_list = len(term_list)
	# Add from left to right
	for t in range(l_term_list):
		exp_value_left = rounding(exp_value_left+term_list[t]*((-1)**t))
		
	print('The value of exp(-5.5) computed left to right is %.5E' %(exp_value_left))

	# Add from right to left
	for t in range(l_term_list):
		exp_value_right = rounding(exp_value_right+term_list[n_max-t-1]*((-1)**(n_max-t)))
		
	print('The value of exp(-5.5) computed right to left is %.5E' %(exp_value_right))

	print('True value of exp(-5.5) is %f' %(np.exp(-5.5)))
	print('The relative error is left-to-right %.6f' %(abs(np.exp(-5.5)-exp_value_left)/np.exp(-5.5)))
	print('The relative error is right-to-left %.6f' %(abs(np.exp(-5.5)-exp_value_right)/np.exp(-5.5)))

	# Make a positive list
	positive_list = []
	negative_list = []
	for t in range(l_term_list):
		if((-1)**t > 0):
			positive_list.append(term_list[t])
		else:
			negative_list.append(term_list[t])

	positive_left = 0.0
	for i in range(len(positive_list)):
		positive_left = rounding(positive_left + positive_list[i])
	negative_left = 0.0
	for i in range(len(negative_list)):
		negative_left = rounding(negative_left + negative_list[i])
	exp_value_left_left = positive_left - negative_left
	print('The value obtained by first summing all the positive and negative independently left-to right %.5E'%(exp_value_left_left))

	positive_right = 0.0
	for i in range(len(positive_list)):
		positive_right = rounding(positive_right + positive_list[len(positive_list)-i-1])
	negative_right = 0.0
	for i in range(len(negative_list)):
		negative_right = rounding(negative_right + negative_list[len(negative_list)-i-1])
	exp_value_right_right = positive_right - negative_right
	print('The value obtained by first summing all the positive and negative independently right to left %.5E'%(exp_value_right_right))
	
	return 0

def problem_2():
	problem_2_positive()
	problem_2_negative()
	return 0
def main():
	problem_2()
	return 0
if __name__ == '__main__':
	main()
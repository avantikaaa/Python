from lshift_input import *

# Your code - begin
def mysum(l):		#Function to calculate the sum of elements of a list l
  add = 0
  for i in l:
	add += i
  return add

def average(l):		#Function to calculate the average of the elements in the list l
  s = mysum(l)*1.0	#Calls the previous function and converts the integer to float(int*float = float)
  return s/len(l)	#Returns average of the numbers

def sqsum(l):			#Function to calculate sum of squares of elements
  s = 0
  s = [s + x*x for x in l]	#Creates a list of squares of elements of the list l
  return mysum(s)

import math			#Declaration of math library as the squareroot(sqrt) function is being used
def sd(l):			#Function to calculate standard division
  N = len(l)
  d = [average(l)-x for x in l]	#creates a list containing the difference between the average and element in list l
  sq = sqsum(d)*1.0		#Calculates the sum of squares of list d and converts the integer to float
  s = math.sqrt(sq/N)		#Standard deviation
  return s
# Your code - end


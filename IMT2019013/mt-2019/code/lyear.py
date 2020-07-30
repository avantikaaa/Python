from lyear_input import *

# Your code - begin
output = False # Your answer should be placed in this variable.
if (inp%4==0):		#Condition 1 -> the year should be divisible by 4
	if(inp%100==0):	#Condition 2 -> the year if divisible by 100, should also be divisible by 400
		if(inp%400==0):
			output = True
	else:		#If the year isn't divisible by 100, but divisible by 4
		output = True
#For all other conditions, the output will hold the boolean value 'False' as it has been declared before the conditions are being executed
# Your code - end

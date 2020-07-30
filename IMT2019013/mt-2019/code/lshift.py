from lshift_input import *

# Your code - begin
for i in range(n):
	k = l.pop(0)	#Stores the value of index 0 of the list in variable k, before removing the element from the list
	l.append(k)	#Adds the value stored in k at the end of the list
output = l
#output = [3,4,5,1,2] # Your answer should be placed in this variable.
# Your code - end

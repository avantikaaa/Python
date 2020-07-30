from Q4input import *

# Your code - begin
l = len(inp)
a = [0]*l
count = 0
n = 0
i = 0
for i in range (len(inp)):	#Checks for zeroes
	if ( inp[i] == 0):	#shifts the 0 to the end
		a[l-n-1	] = 0
		n += 1
	else:			#Puts the next non-zero element in the final list
		a[count] = inp[i]
		count += 1

output = a # should be [1,2,5,7,0,0] for the given input.

# Your code - end
print output

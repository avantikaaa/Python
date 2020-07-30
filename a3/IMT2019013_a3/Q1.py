from Q1input import *

# Your code - begin
d = {}
b = 0
for i in range (len(inp)):	#checks the frequency of each character
	a = inp[i]
	count = 1	
	if ( not inp[i] in d):	#doesn't consider already considered characters
		d[a] = []
		j = i+1
		while(j<len(inp)):
			if (inp[i] == inp[j]):
				count += 1
			j += 1
		d[a] = count



#output = {}
#for i in range (len(d)):
#	c = d[i]
#	output[c] = len(c)

output = d
#output = {1: 3, 2: 5, 3: 2} # This is the answer for the given input.
# Your code - end

print output

from Q3input import *

# Your code - begin

l = len(inp)
inp = inp.lower()
y = 0
d = {}

low = ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


for i in range (0,l):	#loop to check if all letters occur only once
	if (inp[i] in low):
		a = inp[i]
		count = 1	
		if ( not inp[i] in d):
			d[a] = []
			j = i+1
			while(j<len(inp)):
				if (inp[i] == inp[j]):
					count += 1
				j += 1
			d[a] = count

for i in range (l):	#checks if there are any repeating characters
	if (inp[i] in low):	
		if ( d[inp[i]] != 1):
			y=1



if (y==0):
	output = "True"
else:
	output = "False"


# Your code - end
print output

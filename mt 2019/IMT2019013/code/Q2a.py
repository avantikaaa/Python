from Q2input import *

# Your code - begin

for j in Dic2:   
	if (not j in Dic1):  #creates a new entry if not present in Dic1
		Dic1.update({j : Dic2[j]})
	else:
		for i in Dic1: #adds the values of common entries
			if ( i==j):
				Dic1[i] = Dic1[i] + Dic2[j]

		

output = Dic1 # should be {'some':20, 'fuzzy':25, 'data':17, 'logic':0. 'marks':100} for the given input.

# Your code - end
print output

def ndiamond(n):
	a = (n+1)/2
	i = 1
	while(i<a+1):			#Loop to print the first (a) lines of the pattern (number of characters increases with each line)
		s = ""
		j = 0
		while (j<a-i):		#Loop to print spaces
			s = s+" "
			j += 1
		print s,
		j = 0
		s = ""
		while (j<i):		#Loop to create a string with numbers in increasing order
			s = s+str(j+1)
			j += 1
		j -= 1
		while (j>0):		#Loop to add the numbers in decreasing order to the string
			s = s + str(j)
			j -= 1
		print s
		i += 1
	i -= 2
	while (i>0):			#Loop for printing the last (a-1) lines (number of characters decreases with each line)
		s = ""
		j = 0
		while (j<a-i):		#Loop to print spaces
			s = s+" "
			j += 1
		print s,
		j = 0
		s = ""
		while (j<i):		#Loop to create a string with numbers in increasing order
			s = s+str(j+1)
			j += 1
		j -= 1
		while (j>0):		#Loop to add the numbers in decreasing order to the string
			s = s + str(j)
			j -= 1
		print s
		i -= 1



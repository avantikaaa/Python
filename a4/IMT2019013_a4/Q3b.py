def diamond(n):
	a = (n+1)/2
	i = 1
	while(i<a+1):			#Loop for printing the first a lines (number of characters increases with each line)
		s = ""
		j = 0
		while (j<a-i):		#Loop to print spaces
			s = s+" "
			j += 1
		print s,
		j = 0
		s = ""
		while (j<2*i-1):	#Loop to create a string with required number of stars
			s = s+"*"
			j += 1
		print s
		i += 1
	i -= 2
	while (i>0):			#Loop for printing the last (a-1) lines (number of characters decreases with every line)
		s = ""
		j = 0
		while (j<a-i):		#Loop to print spaces
			s = s+" "
			j += 1
		print s,
		j = 0
		s = ""
		while (j<2*i-1):	#Loop to create a string with required number of stars
			s = s+"*"
			j += 1
		print s
		i -= 1



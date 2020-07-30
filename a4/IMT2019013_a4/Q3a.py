def diamond():
	i = 1
	while(i<4):			#Loop for printing the first 3 lines (number of characters increases with each line)
		s = ""
		j = 0
		while (j<3-i):		#Loop to print spaces
			s = s+" "
			j += 1
		print s,		#Continues to print the next string in the same line
		j = 0
		s = ""
		while (j<2*i-1):	#Loop for creating a string containing the required number of stars
			s = s+"*"
			j += 1
		print s
		i += 1
	i = 2
	while (i>0):			#Loop for printing the last 2 lines (number of characters decreases with each line)
		s = ""
		j = 0
		while (j<3-i):		#Loop to print spaces
			s = s+" "
			j += 1
		print s,		#Continues to print in the same line
		j = 0
		s = ""
		while (j<2*i-1):	#Loop for creating a string with the required number of stars
			s = s+"*"
			j += 1
		print s
		i -= 1


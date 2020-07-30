def banner(n):				#To print a message in a banner made of astrix
	i = 0				#Counter
	s = ""
	while (i<len(n)+4):		#Loop for the string containing astrix
		s = s+"*"
		i += 1
	print s				#First banner
	print "* " + str(n) + " *"	#The input string
	print s				#Bottom banner



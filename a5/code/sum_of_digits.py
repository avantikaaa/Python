def sumDigits(n):
## Your code - begin
	if(n/10>0):	
		return (n%10+sumDigits(n/10))	#Recursion
	return n				#Returns the left most digit
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = sumDigits(n)
	print output

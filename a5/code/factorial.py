def factorial(n):
## Your code - begin
	if(n==0):			#Factorial of 0 is 1
		return 1
	return (n*factorial(n-1))	#Returns n* factorial of (n-1)
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = factorial(n)
	print output

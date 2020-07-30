def recurse(ans, n):
## Your code - begin
	if(n==0):
		return int("0"+ans)		#If n=0, adds 0 at the left end of the output
	elif(n>1):
		ans = str(n%2)+ans		#Adds reminder when divided by 2 at the left end
		return recurse(ans, n/2)
	else:
		return int("1"+ans)		#If n=1, adds 1 to the left end
## Your code - end

def decToBin(n):
  return recurse("", n) 

if __name__ == "__main__":
  n = input("Enter number: ")
  output = decToBin(n)
  print output

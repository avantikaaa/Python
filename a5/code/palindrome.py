def recurse(n, i):
## Your code - begin
	s = str(n)
	l = len(s)
	if(i!=(l/2)+1):
		if(s[i]!=s[l-1-i]):			#Compares 'i'th digit from left and right side
			return False			#Loop breaks of the 2 digits aren't equal
		else:
			return (recurse (n, i+1))
	return True
## Your code - end

def isPalindrome(n):
  return recurse(n, 0)
  
if __name__ == '__main__':
	n = raw_input("Enter string: ")
	output = isPalindrome(n)
	print output

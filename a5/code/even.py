def even_elements(l):
## Your code - begin
	even = [x for x in l if x % 2 == 0]	#Adds the element in the list only if the number is even
	return even
## Your code - end
  
if __name__ == "__main__":
  l = range(10)
  print "input = ", l
  print even_elements(l)

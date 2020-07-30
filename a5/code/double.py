def double(l):
## Your code - begin
	doub = [x+x for x in l]		#Adds double of every element to a new list
	return doub
## Your code - end
  
if __name__ == "__main__":
  l = [1, 2, 3]
  print "input = ", l
  print double([1, 2, 3])

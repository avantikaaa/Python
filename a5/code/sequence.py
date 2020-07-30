# Array printing utility function. Feel free to use.
def printArr(arr, k): 
  for i in range(k): 
    print(str(arr[i]) + " "), 
  print
  
def printSeqUtil(n, k, len1, arr): 		#NOTE: When we move on to the next sequence, we overwrite the values of the elements of the existing array instead of making a new array
## Your code - begin
	if(len1==k):				#Prints the array if the array contains 'k' elements
		printArr(arr,k)
		return				#Removes function from the stack
	if(len1==0):
		i=1
	else:
		i=arr[len1-1]+1
	while(i<n+1):				#Maximum value an element can take is 'n'
		arr[len1]=i
		printSeqUtil(n, k, len1+1, arr)
		i+=1



## Your code - end
  
def printSeq(n, k): 
    arr = [0] * k  
    len1 = 0
    printSeqUtil(n, k, len1, arr) 

if __name__ == "__main__":
  n = input("Enter n: ")
  k = input("Enter k: ")
  printSeq(n, k)

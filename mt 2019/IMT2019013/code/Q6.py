from Q6input import *

# Your code - begin
d = {}
length = len(inp)


for i in range (length):		#counts the frequency of each character
	count = 0
	for j in range (length-i):
		if (inp[i]==inp[j+i]):
			count += 1
	if (not inp[i] in d):
		d[inp[i]] = count
	i += 1

list1 = []

for i in d:
	list1.append(d[i])		#creates a list of the frequencies

	
list1.sort()
 
l = []
for i in range (len(list1)):			#removes repeating frequencies
	if (not list1[i] in l):
		l.append(list1[i])
a = []
L = len(l)
for i in range (L):
	b = l[L - i - 1]
	a.append(b)

list2 = []
val = a[N-1]
for i in d:			#creates a list of the characters of the required frequency
	if (d[i]==val):
		list2.append(i)
for i in range (len(list2)):			#for sorting the characters on the basis of their ASCII values
	for j in range (len(list2)):
		if (i!=j):
			a = list2[i]
			b = list2[j]
			if (ord(a)<ord(b)):
				tmp = list2[i]
				list2[i] = list2[j]
				list2[j] = tmp
output = list2[0]  #the first character of the list is the character with the lowest ASCII value



#output = 'e' # This is the expected output for the given input.

# Your code - end
print output

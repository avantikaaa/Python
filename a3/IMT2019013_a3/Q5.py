from Q5input import *

# Your code - begin
alphabets = ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

sets = []

for i in set1:
	i = i.lower()   #converts upper-case letters to lower-case letters
for i in set2:
	i = i.lower()   #converts upper-case letters to lower-case letters
output = 0

for i in set1:
	for j in set2:		#creates strings comprising of elements from first and second set
		m = i+j
		sets.append(m)
output = 0

for j in sets:   #checks if each alphabet is present in the string
	li = list(j)
	y = 0
	for i in range (len(alphabets)):
		if (alphabets[i] in li):
			y += 1
	if (y==26):
		output += 1



#sets = [ # This is the expected value for the given value of set1 and set2.
#  "abcdefghijklmnopqrstuvwxyz",
#  "abcdefghabefgh",
#  "abcdijklmnopqrstuvwxyz",
#  "abcdabefgh",
#  "wxyzijklmnopqrstuvwxyz",
#  "wxyzabefgh"


# Your code - end
print sets
print output


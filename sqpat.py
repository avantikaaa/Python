

def fill(l, index1, index2):
	if(index1>index2):
		return
	fill(l, index1+1, index2-1)
	for i in range (len(l)):
		if(i<index1 or i>index2):
			pass
		else:
			l[i][index1] = index1+1
			l[i][index2] = index1+1
			l[index1][i] = index1+1
			l[index2][i] = index1+1
	return


a = input("Enter number: ")
n, b = 2*a-1,1
l = []
for i in range (n):
	k = []
	for j in range (n):
		k.append(0)
	l.append(k)


fill(l, 0, n-1)

'''
index1 = a-1
index2 = a-1
while(index1>=0 and index2<n):
	for i in range (len(l)):
			l[index1][i] = a
			l[index2][i] = a
			l[i][index1] = a
			l[i][index2] = a
	a-=1
#	b+=1
	index1-=1
	index2+=1
	for i in l:
		for j in i:
			print j,
		print
	print""
'''


for i in l:
	for j in i:
		print j,
	print

from random import randint
n = input("Enter a number: ")
k = input("Enter the number of groups: ")
l = []
number = []
for i in range(n):
    number.append(i+1)

for i in range (k):
    l.append([])
    for j in range (n//k):
        a = randint(0, len(number))
        l[i].append(numbers[a-1])
        number.pop[a-1]

if (len(number)!=0):
    l.append(number)

print l

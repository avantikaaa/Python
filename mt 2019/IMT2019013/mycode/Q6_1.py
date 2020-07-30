from Q6input import *

# Your code - begin

dicti = {}
for key in inp:
    if key != ' ':
        if key in dicti:
            dicti[key] += 1
        else:
            dicti[key] = 1

frequentdicti = {}

for key in dicti:
    if dicti[key] in frequentdicti:
        frequentdicti[dicti[key]].append(key)
    else:
        frequentdicti[dicti[key]] = [key]

counts = list(set(dicti.values()))
counts.sort(reverse = True)

if len(counts) < N:
    output = 'No answer'
else:
    output = min(frequentdicti[ counts[N-1] ])

# Your code - end
print output

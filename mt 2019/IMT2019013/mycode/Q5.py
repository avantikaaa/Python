from Q5input import *

# Your code - begin
output = 0

sets = []
for ele1 in set1:
# b1 : true
# b2 : false
    for ele2 in set2:
    # b3 : true
    # b4 : false
        sets.append(ele1 + ele2)

complete = 'abcdefghijklmnopqrstuvwxyz'

for string in sets:
# b5 : true
# b6 : false
    if len(string) < 26:
    # b7 : true
    # b8 : false
        continue
    count = 0
    for ch in complete:
    # b9 : true
    # b10: false
        if ch in string:
        # b11 : true
            count += 1
        else:
        # b12 : false
            break
    if count == 26:
    # b13 : true
    # b14 : false
        output += 1

# Your code - end
print output

'''
Test Inputs

Q5_1 : set1 = [] set2 = []
coverage: b2, b6

Q5_2 : set1 = ['a'] set2 = ['b']
coverage: b1, b3, b5, b7

Q5_3 : set1 = ['a'] set2 = []
coverage: b1, b4, b5, b7

Q5_4 : set1 = ['abcdefghijklmnopqrstuvwxy'] set2 = ['z']
coverage: b8, b9, b11, b13

Q5_5 : set1 = ['abcdefghijklmnopqrstuvwx'] set2 = ['z']
coverage: b8, b9, b12, b14

'''

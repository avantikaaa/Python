from Q2input import *

# Your code - begin
output = Dic1 # should be {'some':20, 'fuzzy':25, 'data':17, 'logic':0. 'marks':100} for the given input.
for key in Dic2:
# b1 : true
# b2 : false
    if key in output:
    # b3 : true
        output[key] += Dic2[key]
    else:
    # b4 : false
        output[key] = Dic2[key]
# Your code - end
print output

# Q2a_1 : Dic1 = {'some' : 20 } Dic2 = { 'some' : 20 }
# coverage: b1, b3

# Q2a_2 : Dic1 = {'some' : 20 } Dic2 = { 'fuzzy' : 20 }
# coverage: b1, b4

# Q2a_3 : Dic1 ={'some': 5, 'fuzzy':25, 'data':15, 'logic':0},
#         Dic2 = {}
# coverage: b2


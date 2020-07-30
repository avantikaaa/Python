from Q1input import *

# Your code - begin
output = {} # This is the answer for the given input.
for key in inp:
# b1 : true
# b2 : false
    if key in output:
    # b3 : true
        output[key] += 1
    else:
    # b4 : false
        output[key] = 1
# Your code - end

print output

# Q1_1.py : inp = [1]
# coverage = b1, b4

# Q1_2.py : inp = []
# coverage b2

# Q1_3.py : inp = [1, 1]
# coverage b3

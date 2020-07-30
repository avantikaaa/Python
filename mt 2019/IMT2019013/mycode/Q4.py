from Q4input import *

# Your code - begin
output = [] # should be [1,2,5,7,0,0] for the given input.
output += [x for x in inp if x != 0]
output += [x for x in inp if x == 0]
# Your code - end
print output

'''
Test inputs
-----------
Using input space partitioning.
D1 : Number of 0s \in {0, 1, more}
D2 : Number of non-zeros \in {0, 1, more}

Q4_1 : []
coverage: (0, 0)

Q4_2 : [1]
coverage : (0, 1)

Q4_3 : [1, 2]
coverage : (0, more)

Q4_4 : [0]
coverage : (1, 0)

Q4_5 : [0, 1]
coverage : (1, 1)

Q4_6 : [0, 1, 2]
coverage : (1, more)

Q4_7 : [0, 0]
coverage : (more, 0)

Q4_8 : [0, 1, 0]
coverage : (more, 1)

Q4_9 : [0, 1, 0, 2]
coverage : (more, more)



'''

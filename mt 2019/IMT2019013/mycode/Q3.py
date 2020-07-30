from Q3input import *

# Your code - begin
output = True
dicti = []
for ch in inp:
# b1 : true
# b2 : false
    if ch != ' ':
    # b3 : true
    # b4 : false
        if ch not in dicti:
        # b5 : true
            dicti.append(ch)
        else:
        # b6 : false
            output = False
            break
# Your code - end
print output

# Test inputs

# Q3_1 : inp = 'a'
# coverage : b1, b3, b5

# Q3_2 : inp = ''
# coverage : b2

# Q3_3 : inp = 'aa'
# coverage : b6

# Q3_4 : inp = 'a a'

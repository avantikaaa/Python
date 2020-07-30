from Q6input import *

# Your code - begin

dicti = {}
for key in inp:
# b1: true
# b2 : false
    print "b1"
    if key != ' ':
    # b3 : true
    # b4 : false
        print "b3"
        if key in dicti:
        # b5 : true
            print "b5"
            dicti[key] += 1
        else:
        # b6 : false
            print "b6"
            dicti[key] = 1
    else:
      print "b4"
print "b2"
frequentdicti = {}
max_count = 0

for key in dicti:
# b7 : true
# b8 : false
    print "b7"
    max_count = max(max_count, dicti[key])
    if dicti[key] in frequentdicti:
    # b9 : true
        print "b9"
        frequentdicti[dicti[key]].append(key)
    else:
    # b10 : false
        print "b10"
        frequentdicti[dicti[key]] = [key]

print "b8"
N-=1
while(N > 0):
# b11 : true
# b12 : false
    print "b11"
    if max_count in frequentdicti:
    # b13 : true
    # b14 : false
        print "b13"
        N -= 1
    else:
        print "b14"
    max_count -= 1

print "b12"
print frequentdicti
output = min(frequentdicti[max_count])

# Your code - end
print output

'''
Test Inputs
-----------
Q6_1 : N = 1 inp = ""
coverage : b2, b8

Q6_2 :  inp = "a" N = 1
coverage : b1, b3, b6*, b2, b7*, b10*, b12*


Q6_3 :  inp = "aa" N = 1
coverage : b1, b2, b3, b5*, b6, b7, b10, b12


Q6_4 : inp = "a " N = 1
coverage : b1, b3, b6, b4, b2, b7, b8*, b10, b12

Q6_5 : inp = 'aabb' N = 1
coverage : b1 b2 b3 b5 b6 b7 b8 b9 b10 b12*

Q6_6 : inp = 'aabb' N = 1
coverage : b1 b2 b3 b5 b6 b7 b8 b9 b10 b11 b12 b13*
'''

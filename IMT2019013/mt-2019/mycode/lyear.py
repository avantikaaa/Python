from lyear_input import *

# Your code - begin
if inp % 100 == 0:
# b1 - true
  if inp % 400 == 0:
  # b4 - true
    output = True
  else:
  # b5 - false
    output = False
elif inp % 4 == 0:
# b2 - false
  output = True
else:
# b3 - false
  output = False
# Your code - end

'''
inp = 2000
Coverage : b1, b4

inp = 200
Coverage : b1, b5

inp = 4
Coverage : b2

inp = 3
Coverage : b3


'''

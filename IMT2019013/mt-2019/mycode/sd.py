from lshift_input import *

# Your code - begin
def mysum(l):
  s = 0
  for n in l:
    s += n
  return s

def average(l):
  return mysum(l) / float(len(l))

def sqsum(l):
  sq = [n * n for n in l]
  return mysum(sq)

import math
def sd(l):
  mean = average(l)
  diffs = [n - mean for n in l]
  sqdiffs = sqsum(diffs)
  return math.sqrt(float(sqdiffs)/len(l))
# Your code - end

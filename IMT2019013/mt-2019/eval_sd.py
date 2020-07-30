#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval(mf, cf, l):
  subprocess.call(["touch", "mycode/__init__.py"])
  subprocess.call(["touch", "code/__init__.py"])

  if(equals(mf(l), cf(l))):
    return (1,  "eval_" + cf.__name__)
  else:
    return (0, "eval_" + cf.__name__ + ": wrong answer")

@evaluate
def eval_sum1():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.mysum, code.sd.mysum, range(12, 34))

@evaluate
def eval_sum2():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.mysum, code.sd.mysum, range(21, 40))

@evaluate
def eval_average1():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.average, code.sd.average, range(12, 34))

@evaluate
def eval_average2():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.average, code.sd.average, range(21, 40))

@evaluate
def eval_sqsum1():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.sqsum, code.sd.sqsum, range(12, 34))

@evaluate
def eval_sqsum2():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.sqsum, code.sd.sqsum, range(21, 40))

@evaluate
def eval_sd1():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.sd, code.sd.sd, range(12, 34))

@evaluate
def eval_sd2():
  import code.sd
  import mycode.sd

  return eval(mycode.sd.sd, code.sd.sd, range(21, 40))


eval_tests = testsuite(
  [
    (eval_sum1, 1),
    (eval_sum2, 1),
    (eval_average1, 1),
    (eval_average2, 1),
    (eval_sqsum1, 3),
    (eval_sqsum2, 3),
    (eval_sd1, 5),
    (eval_sd2, 5),
  ])

if __name__ == "__main__":
  print(eval_tests())

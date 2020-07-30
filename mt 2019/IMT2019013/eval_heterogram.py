#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval_n(n):
  subprocess.call(["rm", "mycode/Q3input.py"])
  subprocess.call(["rm", "code/Q3input.py"])
  subprocess.call(["cp", "input/Q3_" + str(n) + ".py", "mycode/Q3input.py"])
  subprocess.call(["cp", "input/Q3_" + str(n) + ".py", "code/Q3input.py"])
  import code.Q3
  import mycode.Q3

  if(equals(code.Q3.output, mycode.Q3.output)):
    return (1, "eval_heterogram.eval_" + str(n))
  else:
    return (0, "eval_heterogram.eval_" + str(n) + ": wrong answer")

@evaluate
def eval_1(): return eval_n(1)

@evaluate
def eval_2(): return eval_n(2)

@evaluate
def eval_3(): return eval_n(3)

@evaluate
def eval_4(): return eval_n(4)

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
    (eval_4, 1)
  ])

if __name__ == "__main__":
  print(eval_tests())

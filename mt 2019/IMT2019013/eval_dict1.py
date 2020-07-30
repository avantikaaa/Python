#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval(n):
  subprocess.call(["rm", "mycode/Q1input.py"])
  subprocess.call(["rm", "code/Q1input.py"])
  subprocess.call(["cp", "input/Q1_" + str(n) + ".py", "mycode/Q1input.py"])
  subprocess.call(["cp", "input/Q1_" + str(n) + ".py", "code/Q1input.py"])
  import code.Q1
  import mycode.Q1

  if(equals(code.Q1.output, mycode.Q1.output)):
    return (1, "eval_" + str(n))
  else:
    return (0, "eval_" + str(n) + ": wrong answer")

@evaluate
def eval_1(): return eval(1)

@evaluate
def eval_2(): return eval(2)

@evaluate
def eval_3(): return eval(3)

eval_tests = testsuite(
  [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 2)
  ])

if __name__ == "__main__":
  print(eval_dict1())

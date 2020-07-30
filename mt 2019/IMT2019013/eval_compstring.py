#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval_n(n):
  qname = "compstring"

  subprocess.call(["rm", "mycode/Q5input.py"])
  subprocess.call(["rm", "code/Q5input.py"])
  subprocess.call(["cp", "input/Q5_" + str(n) + ".py", "mycode/Q5input.py"])
  subprocess.call(["cp", "input/Q5_" + str(n) + ".py", "code/Q5input.py"])
  import code.Q5
  import mycode.Q5

  if(equals(code.Q5.output, mycode.Q5.output)):
    return (1, "eval_" + qname + ".eval_" + str(n))
  else:
    return (0, "eval_" + qname + ".eval_" + str(n) + ": wrong answer")

@evaluate
def eval_1(): return eval_n(1)

@evaluate
def eval_2(): return eval_n(2)

@evaluate
def eval_3(): return eval_n(3)

@evaluate
def eval_4(): return eval_n(4)

@evaluate
def eval_5(): return eval_n(5)

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
    (eval_4, 1),
    (eval_5, 1)
  ])

if __name__ == "__main__":
  print(eval_tests())

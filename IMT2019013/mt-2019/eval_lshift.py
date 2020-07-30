#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval(n):
  subprocess.call(["rm", "mycode/lshift_input.py"])
  subprocess.call(["rm", "code/lshift_input.py"])
  subprocess.call(["cp", "input/lshift_input" + str(n) + ".py", "mycode/lshift_input.py"])
  subprocess.call(["cp", "input/lshift_input" + str(n) + ".py", "code/lshift_input.py"])
  subprocess.call(["cp", "input/lshift_input" + str(n) + ".py", "code/lshift_input.py"])
  subprocess.call(["touch", "mycode/__init__.py"])
  subprocess.call(["touch", "code/__init__.py"])
  import code.lshift
  import mycode.lshift

  if(equals(code.lshift.output, mycode.lshift.output)):
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
    (eval_3, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())

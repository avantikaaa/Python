#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval_n(n):
  qname = "freqchar"

  subprocess.call(["rm", "mycode/Q6input.py"])
  subprocess.call(["rm", "code/Q6input.py"])
  subprocess.call(["cp", "input/Q6_" + str(n) + ".py", "mycode/Q6input.py"])
  subprocess.call(["cp", "input/Q6_" + str(n) + ".py", "code/Q6input.py"])

  import code.Q6_1
  import mycode.Q6_1

  if(equals(code.Q6_1.output, mycode.Q6_1.output)):
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

@evaluate
def eval_6(): return eval_n(6)

eval_tests = testsuite([
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
    (eval_4, 1),
    (eval_5, 1),
    (eval_6, 1)
  ])

if __name__ == "__main__":
  print(eval_tests())

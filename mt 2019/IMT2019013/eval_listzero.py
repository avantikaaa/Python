#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval_n(n):
  qname = "listzero"

  subprocess.call(["rm", "mycode/Q4input.py"])
  subprocess.call(["rm", "code/Q4input.py"])
  subprocess.call(["cp", "input/Q4_" + str(n) + ".py", "mycode/Q4input.py"])
  subprocess.call(["cp", "input/Q4_" + str(n) + ".py", "code/Q4input.py"])
  import code.Q4
  import mycode.Q4

  if(equals(code.Q4.output, mycode.Q4.output)):
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

@evaluate
def eval_7(): return eval_n(7)

@evaluate
def eval_8(): return eval_n(8)

@evaluate
def eval_9(): return eval_n(9)


eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
    (eval_4, 1),
    (eval_5, 1),
    (eval_6, 1),
    (eval_7, 1),
    (eval_8, 1),
    (eval_9, 1)
  ])

if __name__ == "__main__":
  print(eval_tests())

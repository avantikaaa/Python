#!/usr/bin/python

import math
from evaluate import *
import subprocess

def eval(n):
  subprocess.call(["rm", "mycode/hyp_input.py"])
  subprocess.call(["rm", "code/hyp_input.py"])
  subprocess.call(["cp", "input/hyp_input" + str(n) + ".py", "mycode/hyp_input.py"])
  subprocess.call(["cp", "input/hyp_input" + str(n) + ".py", "code/hyp_input.py"])
  subprocess.call(["cp", "input/hyp_input" + str(n) + ".py", "code/hyp_input.py"])
  subprocess.call(["touch", "mycode/__init__.py"])
  subprocess.call(["touch", "code/__init__.py"])
  import code.hyp
  import mycode.hyp

  if(equals(code.hyp.output, mycode.hyp.output)):
    return (1, "eval_" + str(n))
  else:
    return (0, "eval_" + str(n) + ": wrong answer")

@evaluate
def eval_1(): return eval(1)

@evaluate
def eval_2(): return eval(2)

eval_tests = testsuite(
  [
    (eval_1, 1),
    (eval_2, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())

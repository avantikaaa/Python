#!/usr/bin/python
import evaluate

import eval_lyear
import eval_hyp
import eval_lshift
import eval_sd

eval_all = evaluate.evaluator(
  evals = [
    (eval_lyear.eval_tests,  1),
    (eval_hyp.eval_tests,    1),
    (eval_lshift.eval_tests, 3),
    (eval_sd.eval_tests,   5),
  ])

if __name__ == "__main__":
  print(eval_all())

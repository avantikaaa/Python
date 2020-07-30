#!/usr/bin/python
import evaluate

import eval_dict1
import eval_dict2
import eval_heterogram
import eval_listzero
import eval_compstring
import eval_freqchar

eval_all = evaluate.evaluator(
  evals = [
    (eval_dict1.eval_tests,      3),
    (eval_dict2.eval_tests,      4),
    (eval_heterogram.eval_tests, 4),
    (eval_listzero.eval_tests,   4),
    (eval_compstring.eval_tests, 5),
    (eval_freqchar.eval_tests,   5)
  ])

if __name__ == "__main__":
  print(eval_all())

#! usr/bin/python
# -*- coding: utf-8 -*-

import string
import sys

def word_n_gram(n, x):
  x_ws = x.split(" ")
  n_gram = []
  for i in range(len(x_ws) - n + 1):
    m = ""
    for k in range(n):
      if k != n - 1:
        m += x_ws[i + k] + " "
      else:
        m += x_ws[i + k]
    n_gram.append(m)
  return n_gram

def char_n_gram(n, x):
  n_gram = []
  for i in range(len(x) - n + 1):
    m = ""
    for k in range(n):
      m += x[i + k]
    n_gram.append(m)
  return n_gram

if __name__ == "__main__":
  tst_x = "paraparaparadise"
  tst_y = "paragraph"
  bi_x = char_n_gram(2, tst_x)
  bi_y = char_n_gram(2, tst_y)
  X = set(bi_x)
  Y = set(bi_y)
  print "X: " + str(X)
  print "Y: " + str(Y)
  print "和集合: " + str(X.union(Y))
  print "差集合: " + str(X.difference(Y))
  print "積集合: " + str(X.intersection(Y))

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
  tst = "I am an NLPer"
  print "単語バイグラム: " + string.join(word_n_gram(2, tst), "|")
  print "文字バイグラム: " + string.join(char_n_gram(2, tst), "|")

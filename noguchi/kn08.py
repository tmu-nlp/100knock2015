#! usr/bin/python
# -*- coding: utf-8 -*-

import sys

def cipher(x):
  y = ""
  for i in range(len(x)):
    if x[i].islower():
      y += chr(219 - ord(x[i]))
    else:
      y += x[i]
  return y

if __name__ == "__main__":
  tst = "Hello"
  print tst
  print cipher(tst)

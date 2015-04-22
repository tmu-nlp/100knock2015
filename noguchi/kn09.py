#! usr/bin/python
# -*- coding: utf-8 -*-

import random
import string

def word_typoglycemia(x):
  if len(x) == 1:
    return x
  else:
    y = ""
    y += x[0]
    list = []
    for i in range(len(x) - 2):
      list.append(x[i + 1])
    random.shuffle(list)
    for i in range(len(x) - 2):
      y += list[i]
    y += x[len(x) - 1]
    return y

def typoglycemia(x):
  y = []
  x_s = x.split(" ")
  for i in range(len(x_s)):
    y.append(word_typoglycemia(x_s[i]))
  return y

if __name__ == "__main__":
  tst = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
  tst2 =  typoglycemia(tst)
  for word in tst2:
    print word,

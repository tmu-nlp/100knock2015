#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string

if __name__ == "__main__":
  tst = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
  tst_nc = tst.replace(",", "")
  tst_ncp = tst_nc.replace(".", "")
  tst_ar = tst_ncp.split(" ")
  tst_gen = tst_ar
  my_dict = {}

#  print tst_ar
  
  for i in range(len(tst_ar)):
    if i == 0 or (i >= 4 and i <= 8) or i == 14 or i == 15 or i == 18:
     tst_gen[i] =  tst_ar[i][0:1]
    else:
     tst_gen[i] =  tst_ar[i][0:2]

  count = 1

  for word in tst_gen:
    print word,
    my_dict[word] = count
    count += 1
  print"\n"

  print my_dict

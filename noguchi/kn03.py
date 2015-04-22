#! /usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
  count = 0

  tst = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
  tst_nc = tst.replace(",", "")
  tst_ncp = tst_nc.replace(".", "")
  tst_ar = tst_ncp.split(" ")

  for word in tst_ar:
    print len(word),

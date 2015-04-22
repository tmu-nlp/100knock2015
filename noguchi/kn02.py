#! usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

  tst1 = u"パトカー"
  tst2 = u"タクシー"
  tst = ""

  for value in range(4):
    tst += tst1[value]
    tst += tst2[value]

  print tst

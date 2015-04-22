#! usr/bin/python
# -*- coding: utf-8 -*-

def tst(x, y, z):
  r =  "%d時の%sは%.1lf度" % (x, y, z)
  return r

if __name__ == "__main__":
  tst2 = tst(12, "気温", 22.4)
  print tst2

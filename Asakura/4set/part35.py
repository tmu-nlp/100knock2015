#!usr/bin/python
#--*--coding:utf-8--*-- part030 from *

from part30 import *

if __name__ == '__main__':
  mecablist = makelist()
  renlist = []
  flag = True
  for bunlist in mecablist:
      for i,mydict in zip(range(len(bunlist)-1),bunlist):
          if flag:
             renlist.append(mydict['surface'])
          if mydict['pos'] == '名詞' and bunlist[i+1]['pos'] == '名詞':
             renlist.append(bunlist[i+1]['surface'])
             flag = False
          elif len(renlist) > 1:
             strings = '+'.join(renlist)
             print strings
             renlist = []
             flag = True
          else:
             renlist = []
             flag = True

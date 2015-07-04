#!usr/bin/python
#--*--coding:utf-8--*--
from part30 import *
if __name__ == '__main__':
  mecablist = makelist()
  for bunlist in mecablist:
      for mydict in bunlist:
          if mydict['pos'] == '動詞':
              print mydict['base']
  #pprint(mecablist)


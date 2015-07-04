#!usr/bin/python
#--*--coding:utf-8--*--

import sys

def makelist():
  inputfile = open("neko.txt.mecab")
  mydict = {}
  mylist = []
  bunlist = []
  mecablist = []
  
  for line in inputfile:
      line = line.replace('\t',',')
      mylist = line.strip().split(',')
      if mylist[0] == 'EOS':
         mecablist.append(bunlist)
         bunlist = []
         continue
      mydict['surface'] = mylist[0]
      mydict['base'] = mylist[7]
      mydict['pos'] = mylist[1]
      mydict['pos1'] = mylist[2]
      bunlist.append(mydict.copy())
  return mecablist
#結果の確認
def pprint(a):
  for i in a:
      for j in i:
          for k, l in j.items():
              print k, l
if __name__ == '__main__':
    mecablist = makelist()
    pprint(mecablist)

#usr/bin/python
#--*--coding:utf=8--*--
from part30 import *

if __name__ == '__main__':
   mecablist = makelist()
   for bunlist in mecablist:
       length = len(bunlist)-2
       for i,mydict in zip(range(length),bunlist):
           if mydict['pos'] == '名詞' and bunlist[i+1]['base']=='の' and bunlist[i+2]['pos'] == '名詞':
              print mydict['surface'] + bunlist[i+1]['surface'] + bunlist[i+2]['surface']

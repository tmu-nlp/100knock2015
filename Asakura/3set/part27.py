#!usr/bin/python
#--*--coding:utf-8--*--

#026.pyの処理に加えて、テンプレート値からMediaWikiの内部リンクマークアップを除去し、テキストに変換せよ

import sys
import re

if __name__ == '__main__':

  inputfile = open(sys.argv[1],'r')
  flag = False
  mydict = {} 
  re_start = re.compile('\{\{基礎情報')
  re_end = re.compile('\}\}')
  re_temp = re.compile('\|(.+?) = (.+)')
  re_ref = re.compile('(.*)(<ref>.*|<ref.*)')
  re_impact = re.compile('\'\'+')
  re_link = re.compile('(\[\[)|(\]\])')

  for line in inputfile:
      if re_start.match(line) is not None:
         flag = True
         continue
      if re_end.match(line) is not None:
         flag = False
         break
      if flag:
         result = re_temp.search(line)
         if result is not None: 
            key = result.group(1)
            ref = re_ref.search(result.group(2))
            if ref is not None:
               value = ref.group(1)
            else:
               value = result.group(2)
            value = re_impact.sub('',value)
            value = re_link.sub('',value)
            mydict[key] = value
  for key,value in mydict.items():
      print '%s = %s' % (key,value)


#!usr/bin/python
#--*--coding:utf-8--*--

#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し、辞書オブジェクトとして格納せよ

import sys
import re

if __name__ == '__main__':
  inputfile = open(sys.argv[1],'r')
  mydict = {}
  flag = False
  re_start = re.compile('\{\{基礎情報')
  re_end = re.compile('\}\}')
  re_temp = re.compile('\|(.+?) = (.+)') 
  re_ref = re.compile('(.*)(<ref>.*|<ref .*>)')
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
            key = result.group(1)#key = re_temp.search(line).group(1)
            ref = re_ref.search(result.group(2))#ref = re_ref.search(re_temp.search(line).group(2))
            if ref is not None:
               value = ref.group(1)
            else:
               value = result.group(2)
            mydict[key] = value
  for key,value in sorted(mydict.items()):
      print '%s = %s'%(key,value)


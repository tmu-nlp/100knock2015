#!usr/bin/python
#--*--coding:utf-8--*--

#テンプレートの値からMediaWikiマークアップを可能な限り除去し、国の基本情報を整理せよ

import sys
import re


if __name__ == '__main__':
  inputfile = open(sys.argv[1],'r')
  re_start = re.compile('\{\{基礎情報')
  re_end = re.compile('\}\}')
  re_temp = re.compile('\|(.+?) = (.+)')
  re_ref = re.compile('(.*)(<ref>.*|<ref .*)')
  re_impact = re.compile('\'\'+')
  re_link = re.compile('\[\[(([^\|\]]*?\|)|([^\|\]]*?))([^\|\]]*?)\]\]')
  re_lang = re.compile('\{\{lang\|.*?\|(.*?)\}\}')
  re_file = re.compile('\[\[ファイル\:(.+?)\|.*?\|.+\]\]')




  flag = False
  mydict = {}
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
            if re_link.search(value) is not None:
               value = re_link.search(value).group(4)
            if re_lang.search(value) is not None:
               value = re_lang.search(value).group(1)
            if re_file.search(value) is not None:
               value = re_file.search(value).group(1)
            mydict[key] = value


  for key,value in sorted(mydict.items()):
      print '%s = %s' % (key,value)

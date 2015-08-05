#!usr/bin/python
#--*--coding:utf-8--*--

import sys
import re

if __name__ == '__main__':
  category = re.compile('\[\[Category\:.*\]\]')#.は改行以外の任意の文字列にマッチ
  for line in open(sys.argv[1]):
      if category.search(line) is not None:#比較にはisを用いなければならない
          print line.strip()
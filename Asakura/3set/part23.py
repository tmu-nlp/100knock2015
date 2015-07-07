#!usr/bin/python
#--*--coding:utf-8--*--

import sys
import re

inputfile = open(sys.argv[1],'r')
pattern = re.compile('(==+)(.+?)==+')#?の意味：＝＝の部分が３個の時、＝＝＋が＝を２個しか取らずに.+に＝が1個含まれてしまうのを防ぐため
for line in inputfile:
    result = pattern.search(line)
    if result is not None:
       print '%s\t%d' % (result.group(2),len(result.group(1))-1)

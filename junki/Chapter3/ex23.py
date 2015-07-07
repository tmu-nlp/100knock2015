#!usr/bin/python
#--*--coding:utf-8--*--
#セクション名とレベルを表示

import sys
import re

inputfile = open(sys.argv[1],'r')
pattern = re.compile('(==+)(.+?)==+')
for line in inputfile:
    result = pattern.search(line)
    if result is not None:
       print '%s\t%d' % (result.group(2),len(result.group(1))-1)
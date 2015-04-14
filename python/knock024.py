#coding:utf-8
'''
python knock024.py ../Data/knock020/result
'''

import sys
import re

re_file = re.compile('\[\[(File|ファイル)\:(.+?)\|.+\]\]')
for line in open(sys.argv[1]):
    result = re_file.search(line)
    if result is not None:
        print result.group(2)

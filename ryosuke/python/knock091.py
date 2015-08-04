# coding:utf-8
"""
python knock091 ../Data/questions-words.txt
"""

import sys

flag = False
for line in open(sys.argv[1]):
    if line.startswith(':'):
        if flag:
            break
        flag = False
    if line.startswith(': family'):
        flag = True
        continue
    if flag:
        print line.strip()


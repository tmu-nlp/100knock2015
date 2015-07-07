# coding:utf-8
"""
python knock070-2.py ../Data/sentiment.txt
"""

import sys

pcount = 0
ncount = 0
for line in open(sys.argv[1]):
    if line.startswith('-1'):
        ncount += 1
    elif line.startswith('+1'):
        pcount += 1
    else:
        print 'error'
        print line
        exit()
print 'positive:%d, negative:%d' % (pcount, ncount)

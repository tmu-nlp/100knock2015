# coding:utf-8
"""
python knock070.py ../Data/rt-polaritydata/rt-polarity.neg ../Data/rt-polaritydata/rt-polarity.pos
"""

import sys
import random

l = list()
append = l.append
for line in open(sys.argv[1]):
    append('%s %s' % ('-1', line.strip()))

for line in open(sys.argv[2]):
    append('%s %s' % ('+1', line.strip()))

random.shuffle(l)
for line in l:
    print line

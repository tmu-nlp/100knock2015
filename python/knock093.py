# coding:utf-8
"""
python knock093.py ../Data/result/knock093/python/w2v.txt
"""

import sys

all_count = .0
count = .0
for line in open(sys.argv[1]):
    all_count += 1
    spl = line.strip().split()
    if spl[3] == spl[4]:
        count += 1

print 'Accuracy: %f%%' % (100*count/all_count)

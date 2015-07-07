# coding:utf-8
"""
python knock078.py ../Data/result/knock078/python/result.txt
"""

import sys

count = 0
aacc = .0
apre = .0
arec = .0
af = .0
for line in open(sys.argv[1]):
    if line.strip() == '':
        continue
    spl = line.strip().split()
    acc, pre, rec, f = (spl[1][:-1], spl[3][:-1], spl[5][:-1], spl[-1])
    acc, pre, rec, f = (float(acc), float(pre), float(rec), float(f))
    aacc += acc
    apre += pre
    arec += rec
    af += f
    count += 1

print 'Accuracy  %f, precision %f, recall %f, F1 %f' % (aacc/count, apre/count, arec/count, af/count)

# coding:utf-8
"""
python knock082.py ../Data/result/knock081/python/clean.txt
"""

import sys
import random

for line in open(sys.argv[1]):
    spl = line.strip().split()
    for i in range(len(spl)):
        window = random.randint(1, 5)
        b =  [ii+1 for ii in range(window)] + [-(ii+1) for ii in range(window)]
        context_indecis = [ii+i for ii in b if ii+i >= 0 and ii+i < len(spl)]
        print '\t'.join([spl[i]] + [spl[ii] for ii in context_indecis])


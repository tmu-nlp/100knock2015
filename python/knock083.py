# coding:utf-8
"""
python knock083.py ../Data/result/knock082/python/result.txt ../Data/result/knock083/python/result.pkl
"""

import sys
import pickle

uni = dict()
co_occ = dict()

for line in open(sys.argv[1]):
    spl = line.strip().split('\t')
    uni[spl[0]] = uni.get(spl[0], 0) + 1
    for co in spl[1:]:
        key = "%s %s" % (spl[0], co)
        co_occ[key] = co_occ.get(key, 0) + 1
N = len(co_occ.keys())

for w, count in uni.items():
    print w, count 
for co, count in co_occ.items():
    print co, count
print "N:", N

pickle.dump([uni, co_occ, N], open(sys.argv[2], 'w'))


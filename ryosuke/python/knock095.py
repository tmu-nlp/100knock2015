# coding:utf-8
"""
python knock095.py ../Data/result/knock094/python/w2v.txt
"""

import sys

w2rank_hum = dict()
w2rank_w2v = dict()

l = list()
for line in open(sys.argv[1]):
    spl = line.strip().split(',')
    l.append((','.join(spl[:2]), float(spl[2]), float(spl[3])))

# human rank
for rank, (key,_,_) in enumerate(sorted(l, key=lambda x: -x[1])):
    rank = rank + 1
    w2rank_hum[key] = rank

# word2vec rank
for rank, (key,_,_) in enumerate(sorted(l, key=lambda x: -x[2])):
    rank = rank + 1
    w2rank_w2v[key] = rank

# calc spearman
N = len(w2rank_hum.keys())
rho = 1 - (6.0 * sum((w2rank_hum[k] - w2rank_w2v[k])**2 for k in w2rank_hum.keys())) / (N**3 - N)
print rho


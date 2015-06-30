# coding:utf-8
"""
python knock075.py ../Data/result/knock073/python/model073.txt
"""

import sys

lower = list()
higher = list()
lim = 10

for line in open(sys.argv[1]):
    if line.startswith('@'):
        continue
    weight = line.strip().split()
    weight[0] = float(weight[0])
    if len(lower) < lim:
        lower.append(weight)
    elif weight[0] < sorted(lower, key=lambda x: x[0])[-1][0]:
        lower.remove(sorted(lower, key=lambda x: x[0])[-1])
        lower.append(weight)
        
    if len(higher) < lim:
        higher.append(weight)
    elif weight[0] > sorted(higher, key=lambda x: x[0])[0][0]:
        higher.remove(sorted(higher, key=lambda x: x[0])[0])
        higher.append(weight)

for w in sorted(lower, key=lambda x: x[0]):
    print w[0], w[1]
print
for w in sorted(higher, key=lambda x: -x[0]):
    print w[0], w[1]

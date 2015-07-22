# coding:utf-8
"""
python knock084.py ../Data/result/knock083/python/result.pkl ../Data/result/knock084/python/X.pkl ../Data/result/knock084/python/word2id.pkl
"""

import sys
import pickle
import scipy.sparse as sp
import math

uni, con, co_occ, N = pickle.load(open(sys.argv[1]))
#Vt = len(uni.keys())
#Vc = len(con.keys())
Vt = 10000
Vc = 10000
X = sp.lil_matrix((Vt, Vc))
word2id = dict()

must = ["United_States", "U.S", "England", "Spain", "Madrid", "Athens", "Greece"]
for i, tok in enumerate(must + uni.keys()):
    word2id[tok] = i
    if i == Vt:
        break
    for j, co in enumerate(con.keys()):
        if j == Vc:
            break
        if co_occ.get('%s %s' % (tok, co), 0) >= 10:
            # ppmi
            X[i, j] = max(0, math.log((1.0*N*co_occ['%s %s' % (tok, co)])/(uni[tok]*con[co]), 2))

print X
pickle.dump(X, open(sys.argv[2], 'w'))
pickle.dump(word2id, open(sys.argv[3], 'w'))


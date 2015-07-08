# coding:utf-8
"""
python knock084.py ../Data/result/knock083/python/result.pkl ../Data/result/knock084/python/X.pkl
"""

import sys
import pickle
import scipy.sparse as sp
import math

uni, con, co_occ, N = pickle.load(open(sys.argv[1]))
Vt = len(uni.keys())
Vc = len(con.keys())
X = sp.lil_matrix((Vt, Vc))
for i, tok in enumerate(uni.keys()):
    for j, co in enumerate(con.keys()):
        if co_occ.get('%s %s' % (tok, co), 0) >= 10:
            # ppmi
            X[i, j] = max(0, math.log((1.0*N*co_occ['%s %s' % (tok, co)])/(uni[tok]*con[co]), 2))
        else:
            X[i, j] = 0
print X
pickle.dump(X, open(sys.argv[2], 'w'))


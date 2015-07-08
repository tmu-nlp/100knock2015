# coding:utf-8
"""
python knock084.py ../Data/result/knock083/result.pkl ../Data/result/knock084/X.pkl
"""

import pickle
import scipy
import math

uni, con, co_occ, N = pickle.load(open(sys.argv[1]))
Vt = len(uni.keys())
Vc = len(con.keys())
X = scipy.sparse.lil_matrix((Vt, Vc))
for i, tok in enumerate(uni.keys()):
    for j, co in enumerate(co.keys()):
        if co_occ.get('%s %s' % (tok, co), 0) >= 10:
            # ppmi
            X[i, j] = max(0, math.log((1.0*N*co_occ['%s %s' % (tok, co)])/(uni[tok]*con[co]), 2))
        else:
            X[i, j] = 0
print X
pickle.dump(X, open(sys.argv[2], 'w'))


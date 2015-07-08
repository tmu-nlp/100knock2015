# coding:utf-8
"""
python knock085.py ../Data/result/knock084/python/X.pkl ../Data/result/knock085/python/Xpca.pkl
"""

import sys
import pickle
import scipy
import sklearn.decomposition

dim = 300
X = pickle.load(open(sys.argv[1]))
pca = sklearn.decomposition.PCA(dim)
Xpca = pca.fit_transform(X)
print Xpca
pickle.dump(Xpca, open(sys.argv[2], 'w'))

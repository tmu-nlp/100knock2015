# coding:utf-8
"""
python knock087.py ../Data/result/knock085/python/Xpca.pkl ../Data/result/knock083/python/result.pkl
"""

import sys
import pickle
import scipy.spatial.distance as dis

Xpca = pickle.load(open(sys.argv[1]))
uni,_,_,_ = pickle.load(open(sys.argv[2]))

i = uni.keys().index('United_States')
ii = uni.keys().index('U.S')
 
print dis.cosine(X[i,], X[ii,])


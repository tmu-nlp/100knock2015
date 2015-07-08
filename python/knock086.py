# coding:utf-8
"""
python knock086.py ../Data/result/knock085/python/Xpca.pkl ../Data/result/knock083/python/result.pkl
"""

import sys
import pickle

Xpca = pickle.load(open(sys.argv[1]))
uni,_,_,_ = pickle.load(open(sys.argv[2]))

i = uni.keys().index('United_States')
print X[i,]


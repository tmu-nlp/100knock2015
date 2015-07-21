# coding:utf-8
"""
python knock086.py ../Data/result/knock085/python/Xpca.pkl ../Data/result/knock084/python/word2id.pkl
"""

import sys
import pickle

Xpca = pickle.load(open(sys.argv[1]))
word2id = pickle.load(open(sys.argv[2]))

i = word2id['United_States']
print Xpca[i]


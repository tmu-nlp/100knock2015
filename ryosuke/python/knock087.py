# coding:utf-8
"""
python knock087.py ../Data/result/knock085/python/Xpca.pkl ../Data/result/knock084/python/word2id.pkl
"""

import sys
import pickle
import numpy


def cossim(x,y):
    return numpy.sum(x*y) / (numpy.sqrt(numpy.sum(x*x)) * numpy.sqrt(numpy.sum(y*y)))

Xpca = pickle.load(open(sys.argv[1]))
word2id = pickle.load(open(sys.argv[2]))

i = word2id['United_States']
ii = word2id['U.S']
 
print cossim(Xpca[i], Xpca[ii])


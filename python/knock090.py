# coding:utf-8
"""
python knock090.py ../Data/result/knock090/python/vectors.bin
"""

import sys
from gensim.models import word2vec

def knock086():
    print 'knock086'
    print model.__getitem__('United_States')

def knock087():
    print 'knock087'
    print model.n_similarity('United_States', 'U.S')

def knock088():
    print 'knock088'
    for w,s in  model.most_similar(['England']):
        print w, s

def knock089():
    print 'knock089'
    for w,s in  model.most_similar(['Spain', 'Athens'], ['Madrid']):
        print w, s

model = word2vec.Word2Vec.load_word2vec_format(sys.argv[1], binary=True)
knock086()
print
knock087()
print
knock088()
print
knock089()

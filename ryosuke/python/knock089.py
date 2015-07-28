# coding:utf-8
"""
python knock089.py ../Data/result/knock085/python/Xpca.pkl ../Data/result/knock084/python/word2id.pkl
"""

import sys
import pickle
import numpy


def cossim(x,y):
    return numpy.sum(x*y) / (numpy.sqrt(numpy.sum(x*x)) * numpy.sqrt(numpy.sum(y*y)))


def similer_words(query_v, Xpca, word2id, n=10):
    id2word = {v: k for k, v in word2id.items()}
    similers = list() # (word, vector, similarity)
    for i, v in enumerate(Xpca):
        if len(similers) < n:
            similers.append((id2word[i], v, cossim(v, query_v)))
            similers = sorted(similers, key=lambda x: -x[2])
        else: 
            # compare
            new_sim = cossim(v, query_v)
            for j,(_,_,sim) in enumerate(similers):
                if sim < new_sim:
                    similers.pop(j)
                    similers.insert(j, (id2word[i], v, new_sim))
                    break
    return similers

if __name__ == '__main__':
    Xpca = pickle.load(open(sys.argv[1]))
    word2id = pickle.load(open(sys.argv[2]))

    spain = Xpca[word2id['Spain']]
    madrid = Xpca[word2id['Madrid']]
    athens = Xpca[word2id['Athens']]
    query = spain - madrid + athens
    print 'query: Spain - Madrid + Athens'
    for w,v,s in similer_words(query, Xpca, word2id):
        print w, s

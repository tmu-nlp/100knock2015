# coding:utf-8
"""
python knock094.py ../Data/wordsim353/combined.csv ../Data/result/knock090/python/vectors.bin
"""

import sys
from gensim.models import word2vec

model = word2vec.Word2Vec.load_word2vec_format(sys.argv[2], binary=True)

for line in open(sys.argv[1]):
    words = line.strip().split(',')
    if not model.__contains__(words[0]) or not model.__contains__(words[1]):
        continue
    sim = model.similarity(words[0], words[1])
    print line.strip()+','+str(sim)


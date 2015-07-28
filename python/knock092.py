# coding:utf-8
"""
python knock092.py ../Data/result/knock091/python/family.txt ../Data/result/knock090/python/vectors.bin ../Data/result/knock085/python/Xpca10000_2.pkl ../Data/result/knock084/python/word2id10000_2.pkl ../Data/result/knock092/python/w2v.txt ../Data/result/knock092/python/Xpca.txt
"""

import sys
import pickle
from gensim.models import word2vec
from knock088 import *

Xpca = pickle.load(open(sys.argv[3]))
word2id = pickle.load(open(sys.argv[4]))
w2v_model = word2vec.Word2Vec.load_word2vec_format(sys.argv[2], binary=True)

# word2vec
f = open(sys.argv[5], 'w')
for line in open(sys.argv[1]):
    words = line.strip().split()
    if not w2v_model.__contains__(words[0]) or not w2v_model.__contains__(words[1]) or not w2v_model.__contains__(words[2]):
        continue
    f.write(line.strip()+' '+w2v_model.most_similar([words[1], words[2]],[words[0]], topn=1)[0][0].encode('utf-8')+'\n')
f.close()

f = open(sys.argv[6], 'w')
# Xpca
for line in open(sys.argv[1]):
    words = line.strip().split()
    if not words[0] in word2id or not words[1] in word2id or not words[2] in word2id:
        continue
    q = Xpca[word2id[words[1]]] - Xpca[word2id[words[0]]] + Xpca[word2id[words[2]]]
    f.write(line.strip()+' '+similer_words(q, Xpca, word2id)[0][0]+ '\n')
f.close()


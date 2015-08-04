# coding:utf-8
"""
python knock096.py ../Data/result/knock090/python/vectors.bin ../Data/country_name_list.txt ../Data/result/knock096/python/countly.pkl
"""

import sys
import pickle
from gensim.models import word2vec

dic = dict()
model = word2vec.Word2Vec.load_word2vec_format(sys.argv[1], binary=True)
for line in open(sys.argv[2]):
    word = '_'.join(line.strip().split())
    if model.__contains__(word):
        dic[word] = model[word]
pickle.dump(dic, open(sys.argv[3], 'w'))

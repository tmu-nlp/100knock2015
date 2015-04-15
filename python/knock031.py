#coding:utf-8
'''
python knock031.py ../Data/knock030/result.pkl
'''

import sys
import pickle

doc = pickle.load(open(sys.argv[1]))

for sent in doc:
    for m in sent:
        if m['pos'] == '動詞':
            print m['surface']

# coding:utf-8
'''
python knock034.py ../Data/neko.txt.mecab
'''

import sys
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])
dummy = {'surface': None, 'pos': None}

for sent in doc:
    prev = dummy
    preprev = dummy
    for m in sent:
        if m['pos'] == '名詞' and prev['surface'] == 'の' and preprev['pos'] == '名詞':
            print preprev['surface'], prev['surface'], m['surface']
        preprev = prev
        prev = m

# coding:utf-8
'''
python knock035.py ../Data/neko.txt.mecab
'''

import sys
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])

for sent in doc:
    nouns = list()
    for m in sent:
        if m['pos'] == '名詞':
            nouns.append(m)
        elif nouns:
            print ' '.join(m['surface'] for m in nouns)
            nouns = list()

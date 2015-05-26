# coding:utf-8
'''
python knock032.py ../Data/neko.txt.mecab
'''

import sys
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])

for sent in doc:
    for m in sent:
        if m['pos'] == '動詞':
            print m['base']

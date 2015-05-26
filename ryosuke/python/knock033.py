# coding:utf-8
'''
python knock033.py ../Data/neko.txt.mecab
'''

import sys
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])

for sent in doc:
    for m in sent:
        if m['pos'] == '名詞' and m['pos1'] == 'サ変接続':
            print m['surface'], m['base']

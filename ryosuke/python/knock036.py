# coding:utf-8
'''
python knock036.py ../Data/neko.txt.mecab
'''

import sys
from collections import Counter
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])
words = [m['surface'] for sent in doc for m in sent]

for word, count in Counter(words).most_common():
    print count, word


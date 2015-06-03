# coding:utf-8
'''
python knock039.py ../Data/neko.txt.mecab
'''

import sys
from collections import Counter
import matplotlib.pyplot as plt
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])
words = [m['surface'] for sent in doc for m in sent]

names, counts = zip(*Counter(words).most_common())

plt.bar(range(1, len(names)+1), counts)
plt.xscale('log')
plt.yscale('log')
plt.show()

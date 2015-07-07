# coding:utf-8
'''
python knock037.py ../Data/neko.txt.mecab
'''

import sys
from collections import Counter
import matplotlib.pyplot as plt
import knock030 as marujirou

doc = marujirou.get_morphs(sys.argv[1])
words = [m['surface'] for sent in doc for m in sent]

names, counts = zip(*Counter(words).most_common()[:10])

plt.bar(range(len(names)), map(lambda x: int(x), counts), align='center')
plt.xticks(range(len(names)), map(lambda x: x.decode('utf-8'), names))
plt.xlim(xmin=-1)
plt.show()

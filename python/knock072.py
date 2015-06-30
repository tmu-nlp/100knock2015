# coding:utf-8
"""
python knock072.py ../Data/sentiment.txt
"""

import sys
from stemming.porter2 import stem
from knock071 import is_stop

for line in open(sys.argv[1]):
    spl = line.strip().split()
    label = spl[0]
    text = spl[1:]
    feature = (stem(tok) for tok in text if not is_stop(tok))
    print '%s %s' % (label, ' '.join(feature))

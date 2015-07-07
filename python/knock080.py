# coding:utf-8
"""
python knock080.py ../Data/enwiki-20150112-400-r100-10576.txt
"""

import sys
import re

re_symbol = re.compile('[.,!?;:()\[\]]')

for line in open(sys.argv[1]):
    spl = [re_symbol.sub('', tok) for tok in line.strip().split()]
    print ' '.join(tok for tok in spl if tok)

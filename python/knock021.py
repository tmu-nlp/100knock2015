'''
python knock021.py ../Data/knock020/result
'''

import sys
import re

category = re.compile('\[\[Category\:.*\]\]')
for line in open(sys.argv[1]):
    if category.search(line) is not None:
        print line.strip()

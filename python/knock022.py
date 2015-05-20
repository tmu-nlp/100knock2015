'''
python knock022.py ../Data/knock020/result
'''

import sys
import re

category = re.compile('\[\[Category\:(((?P<cat1>.*)\|+.*)|(?P<cat2>.*))\]\]')
for line in open(sys.argv[1]):
    result = category.search(line)
    if result is not None:
        print  result.group('cat1') if result.group('cat2') is None else result.group(4)

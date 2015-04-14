'''
python knock022.py ../Data/knock020/result
'''

import sys
import re

category = re.compile('\[\[Category\:(((.*)\|+.*)|(.*))\]\]')
for line in open(sys.argv[1]):
    result = category.search(line)
    if result is not None:
        print  result.group(3) if result.group(4) is None else result.group(4)

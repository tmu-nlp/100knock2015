'''
python knock023.py ../Data/knock020/result
'''

import sys
import re

section = re.compile('(==+)(.+?)==+')
for line in open(sys.argv[1]):
    result = section.search(line)
    if result is not None:
        print '%s\t%d' % (result.group(2), len(result.group(1)) - 1)

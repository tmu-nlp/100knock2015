'''
python knock021.py ../Data/knock020/result
'''

import sys

for line in open(sys.argv[1]):
    if 'Category' in line:
        print line.strip()

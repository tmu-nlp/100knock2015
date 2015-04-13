'''
python knock014.py ../Data/hightemp.txt [n]
'''

import sys

count = 0
for line in open(sys.argv[1]):
    print line.strip()
    count += 1
    if count == int(sys.argv[2]):
        break

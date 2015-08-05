'''
python knock018.py ../Data/hightemp.txt
'''

import sys
lines = list()
for line in open(sys.argv[1]):
    lines.append(line.strip().split('\t'))

for spl in sorted(lines, key=lambda x: -float(x[2])):
    print ' '.join(spl)

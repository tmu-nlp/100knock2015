'''
python knock015.py ../Data/hightemp.txt [n]
'''

import sys

count = 0
limit = int(sys.argv[2])
result = list()
for line in open(sys.argv[1]):
    result.append(line.strip())
    if count >= limit:
        result.pop(0)
    count += 1
    

for line in result:
    print line

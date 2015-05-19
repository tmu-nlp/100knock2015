'''
python knock017.py col1.txt
'''
import sys

d = dict()
for line in open(sys.argv[1]):
    d[line.strip()] = 0

for key in d.keys():
    print key

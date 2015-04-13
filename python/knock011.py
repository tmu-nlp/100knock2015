'''
python knock011.py ../Data/hightemp.txt
'''

import sys

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        print line.strip().replace('\t', ' ')

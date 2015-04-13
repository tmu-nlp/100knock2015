'''
python knock012.py ../Data/hightemp.txt ../Data/col1.txt ../Data/col2.txt
'''

import sys

if __name__ == '__main__':
    col1 = open(sys.argv[2], "w")
    col2 = open(sys.argv[3], "w")
    for line in open(sys.argv[1]):
        spl = line.strip().split('\t')
        print >>col1, spl[0]
        print >>col2, spl[1]


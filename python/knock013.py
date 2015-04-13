'''
python knock013.py Data/col1.txt Data/col2.txt 
'''

import sys

if __name__ == '__main__':
    for line1, line2 in zip(open(sys.argv[1]), open(sys.argv[2])):
        print '%s\t%s' % (line1.strip(), line2.strip())

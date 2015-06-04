# coding:utf-8
'''
python knock051.py ../Data/knock050.result
'''

import sys


def main(in_fname):
    for line in open(in_fname):
        print '\n'.join(line.split(' '))

if __name__ == '__main__':
    main(sys.argv[1])

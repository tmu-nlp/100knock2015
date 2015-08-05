# coding:utf-8

import sys


def main(in_fname):
    for line in open(in_fname):
        print '\n'.join(line.split(' '))

if __name__ == '__main__':
    main(sys.argv[1])
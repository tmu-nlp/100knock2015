# coding:utf-8
'''
python knock050.py ../Data/nlp.txt
'''

import sys
import re


def main(in_fname):
    re_sent = re.compile('(?P<end>\.|\;|\:|\?|\!) (?P<start>[A-Z])')
    for line in open(in_fname):
        if line == '\n':
            continue
        print re_sent.sub(lambda m: '%s\n%s' % (m.group('end'), m.group('start')),line.strip())
         

if __name__ == '__main__':
    main(sys.argv[1])

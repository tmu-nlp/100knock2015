# coding:utf-8
'''
python knock040.py ../Data/neko.txt.cabocha
'''

import sys


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '%s\t%s,%s,%s' % (self.surface, self.pos, self.pos1, self.base)

def main(in_fname):
    sent = list()
    doc = list()
    for line in open(in_fname):
        if line.startswith('* '):
            continue
        if line.startswith('EOS'):
            if sent:
                doc.append(sent)
                sent = list()
            continue
        spl = line.split('\t')
        surface = spl[0]
        spl = spl[1].split(',')
        pos = spl[0]
        pos1 = spl[1]
        # unknown word
        if len(spl) == 6:
            base = "*"
        else:
            base = spl[10]
        sent.append(Morph(surface, base, pos, pos1))

    # output
    for morph in doc[2]:
        print morph

if __name__ == '__main__':
    main(sys.argv[1])

# coding:utf-8
'''
python knock041.py ../Data/neko.txt.cabocha
'''

import sys


class Chunk():
    def __init__(self, dst, morphs=None, srcs=None):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
        if morphs is None:
            self.morphs = list()
        if srcs is None:
            self.srcs = list()

    def append_morph(self, morph):
        self.morphs.append(morph)

    def append_srcs(self, src):
        self.srcs.append(src)
    
    def get_raw(self, myfilter=lambda m: True):
        return ''.join(mm.surface for mm in filter(myfilter, (m for m in self.morphs)))

    def hasNoun(self):
        return any(m.pos=='名詞' for m in self.morphs)

    def hasVerb(self):
        return any(m.pos=='動詞' for m in self.morphs)


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '%s\t%s,%s,%s' % (self.surface, self.pos, self.pos1, self.base)


def create_doc(in_fname):
    doc = list()
    sent = list()
    for line in open(in_fname):
        if line.startswith('* '):
            chunk = Chunk(int(line.split(' ')[2][:-1]))
            sent.append(chunk)
            continue
        if line.startswith('EOS'):
            if sent:
                doc.append(sent)
                # update srcs
                for i, chunk in enumerate(sent):
                    if chunk.dst != -1:
                        sent[chunk.dst].append_srcs(i)
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
        # update morphs
        chunk.append_morph(Morph(surface, base, pos, pos1))
    return doc


def main(in_fname):
    doc = create_doc(in_fname)
    # output
    for i, chunk in enumerate(doc[7]):
        print '%d %d\t%s' % (i, chunk.dst, chunk.get_raw())

if __name__ == '__main__':
    main(sys.argv[1])

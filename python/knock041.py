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

    def hasCase(self):
        return any(m.pos=='助詞' for m in self.morphs)

    def get_first_verb(self):
        for m in self.morphs:
            if m.pos == '動詞':
                return m

    def get_case(self):
        return filter(lambda m: m.pos=='助詞', self.morphs)[-1]

    def isSahenWoVerb(self):
        for i, m in enumerate(self.morphs):
            if m.pos == '名詞' and m.pos2 == 'サ変可能':
                try:
                    m1 = self.morphs[i+1]
                    m2 = self.morphs[i+2]
                    if m1.pos == '助詞' and m1.surface == 'を' and m2.pos == '動詞':
                        return True 
                except IndexError:
                    continue

    def get_sahen_wo_verb(self):
        for i, m in enumerate(self.morphs):
            if m.pos == '名詞' and m.pos2 == 'サ変可能':
                try:
                    m1 = self.morphs[i+1]
                    m2 = self.morphs[i+2]
                    if m1.pos == '助詞' and m1.surface == 'を' and m2.pos == '動詞':
                        return '%s%s%s' % (m.surface, m1.surface, m2.base)
                except IndexError:
                    continue

class Morph():
    def __init__(self, surface, base, pos, pos1, pos2):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        self.pos2 = pos2

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
        pos2 = spl[2]
        # unknown word
        if len(spl) == 6:
            base = "*"
        else:
            base = spl[10]
        # update morphs
        chunk.append_morph(Morph(surface, base, pos, pos1, pos2))
    return doc


def main(in_fname):
    doc = create_doc(in_fname)
    # output
    for i, chunk in enumerate(doc[7]):
        print '%d %d\t%s' % (i, chunk.dst, chunk.get_raw())

if __name__ == '__main__':
    main(sys.argv[1])

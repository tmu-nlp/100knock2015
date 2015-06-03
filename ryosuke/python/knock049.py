# coding:utf-8
'''
python knock049.py ../Data/neko.txt.cabocha
'''

import sys
import itertools
import knock041 as marujirou


def get_path(sent, ch1, ch2):
    ch1_walk = list()
    # walk chunk1
    ch = ch1
    while ch.dst != -1:
        ch = sent[ch.dst]
        if ch.index == ch2.index:
            outputs = [ch1.replace_noun('X')]
            outputs += [chh.get_raw() for chh in ch1_walk]
            outputs += [ch2.replace_noun('Y')]
            return '->'.join(outputs)
        ch1_walk.append(ch)
    
    # walk chunk2
    ch = ch2
    ch2_walk = list()
    while ch.dst != -1:
        ch = sent[ch.dst]
        if ch in ch1_walk:
            outputx = [ch1.replace_noun('X')]
            outputx += [chh.get_raw() for chh in ch1_walk[:ch1_walk.index(ch)]]
            outputy = [ch2.replace_noun('Y')]
            outputy += [chh.get_raw() for chh in ch2_walk]
            return ' | '.join([' -> '.join(outputx), ' -> '.join(outputy), ch.get_raw()])
        ch2_walk.append(ch)
    return 'None'


def get_all_path(sent, nps):
    for np1, np2 in itertools.combinations(nps, 2):
        yield get_path(sent, np1, np2)

def main(in_fname):
    doc = marujirou.create_doc(in_fname)
    for sent in doc:
        nps = list()
        for chunk in sent:
            if chunk.hasNoun():
                nps.append(chunk)
        for path in get_all_path(sent, nps):
            print path

if __name__ == '__main__':
    main(sys.argv[1])

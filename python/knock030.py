# coding:utf-8
"""python python/knock030.py ../Data/neko.txt.mecab [out.pkl]."""

import sys


def get_morphs(mecab_out):

    doc = list()
    sent = list()
    for line in open(mecab_out):
        spl_tmp = line.strip().split('\t')
        # EOSがきたら一文の終わり
        if spl_tmp[0] == 'EOS':
            if len(sent) == 0:
                continue
            doc.append(sent)
            sent = list()
            continue
        
        spl = spl_tmp[1].split(',')
        spl.insert(0, spl_tmp[0])
    
        morph = dict()
        morph['surface'] = spl[0]
        morph['base'] = spl[3]
        morph['pos'] = spl[1]
        morph['pos1'] = spl[7]
        
        sent.append(morph)

    return doc


def main():
    doc = get_morphs(sys.argv[1])

    for sent in doc:
        for m in sent:
            print '%s, %s, %s, %s' % (m['surface'], m['base'], m['pos'], m['pos1'])


if __name__ == '__main__':
    main()

# coding:utf-8
"""
mecab with ipadic
python python/knock030.py ../Data/neko.txt.mecab
"""

import sys
import re


def get_morphs(mecab_out):
    doc = list()
    sent = list()
    re_mecab = re.compile('(?P<surface>.*?)\t(?P<pos>.*?),(?P<pos1>.*?),(.*?,){4}(?P<base>.*?),.*')
    re_mecab_unk = re.compile('(?P<surface>.*?)\t(?P<pos>.*?),(?P<pos1>.*?),.*')

    for line in open(mecab_out):
        # EOSが終わり
        if line.startswith('EOS'):
            if sent: 
                doc.append(sent)
                sent = list()
            continue
        match = re_mecab.search(line)
        unk_match = re_mecab_unk.search(line) 
        morph = dict()
        if match is not None:
            morph['surface'] = match.group('surface')
            morph['base'] = match.group('base')
            morph['pos'] = match.group('pos')
            morph['pos1'] = match.group('pos1')
            sent.append(morph)
        elif unk_match is not None:
            morph['surface'] = unk_match.group('surface')
            morph['base'] = '*'
            morph['pos'] = unk_match.group('pos')
            morph['pos1'] = unk_match.group('pos1')
            sent.append(morph)
        else:
            print "not match: ", line,
    return doc

#    for line in open(mecab_out):
#        spl_tmp = line.strip().split('\t')
#        # EOSがきたら一文の終わり
#        if spl_tmp[0] == 'EOS':
#            if len(sent) == 0:
#                continue
#            doc.append(sent)
#            sent = list()
#            continue
#
#        spl = spl_tmp[1].split(',')
#        spl.insert(0, spl_tmp[0])
#
#        morph = dict()
#        morph['surface'] = spl[0]
#        morph['base'] = spl[3]
#        morph['pos'] = spl[1]
#        morph['pos1'] = spl[7]
#
#        sent.append(morph)


def main():
    doc = get_morphs(sys.argv[1])

    for sent in doc:
        for m in sent:
            print '%s, %s, %s, %s' % (
                m['surface'], m['base'], m['pos'], m['pos1'])


if __name__ == '__main__':
    main()

#!/usr/bin/python
#-*-coding:utf-8-*-

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

def main():
    doc = get_morphs(sys.argv[1])

    for sent in doc:
        for m in sent:
            print '%s, %s, %s, %s' % (
                m['surface'], m['base'], m['pos'], m['pos1'])


if __name__ == '__main__':
    main()
# coding:utf-8
'''
python knock043.py ../Data/neko.txt.cabocha
'''

import sys
import knock041 as marujirou


def main(in_fname):
    doc = marujirou.create_doc(in_fname)
    symbol_filter = lambda m: m.pos != '補助記号'
    for sent in doc:
        for chunk in sent:
            if chunk.dst != -1 and chunk.hasNoun() and sent[chunk.dst].hasVerb():
                print '%s\t%s' % (chunk.get_raw(symbol_filter), sent[chunk.dst].get_raw(symbol_filter))

if __name__ == '__main__':
    main(sys.argv[1])

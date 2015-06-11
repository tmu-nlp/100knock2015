# coding:utf-8
'''
python knock048.py ../Data/neko.txt.cabocha
'''

import sys
import knock041 as marujirou


def main(in_fname):
    doc = marujirou.create_doc(in_fname)
    for sent in doc:
        for chunk in sent:
            if chunk.dst != -1 and chunk.hasNoun():
                outputs = chunk.get_raw()
                while chunk.dst != -1:
                    outputs += ' -> %s' % sent[chunk.dst].get_raw()
                    chunk = sent[chunk.dst]
                print '%s' % outputs

if __name__ == '__main__':
    main(sys.argv[1])

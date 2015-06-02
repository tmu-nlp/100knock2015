# coding:utf-8
'''
python knock045.py ../Data/neko.txt.cabocha
'''

import sys
import knock041 as marujirou


def main(in_fname):
    doc = marujirou.create_doc(in_fname)
    for sent in doc:
        for chunk in sent:
            if chunk.srcs and chunk.hasVerb():
                pred = chunk.get_first_verb().base 
                cases = sorted([sent[src].get_case().base for src in chunk.srcs if sent[src].hasCase()])
                if not cases:
                    continue
                print '%s\t%s' % (pred, ' '.join(cases)) 

if __name__ == '__main__':
    main(sys.argv[1])

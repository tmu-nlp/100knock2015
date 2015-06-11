# coding:utf-8
'''
python knock047.py ../Data/neko.txt.cabocha
'''

import sys
import knock041 as marujirou


def main(in_fname):
    doc = marujirou.create_doc(in_fname)
    for sent in doc:
        for chunk in sent:
            if chunk.srcs and chunk.isSahenWoVerb():
                pred = chunk.get_sahen_wo_verb()
                cases_args = sorted([(sent[src].get_case().base, sent[src].get_raw()) for src in chunk.srcs if sent[src].hasCase()])
                if not cases_args:
                    continue
                cases, args = zip(*cases_args)
                print '%s\t%s\t%s' % (pred, ' '.join(cases), ' '.join(args)) 

if __name__ == '__main__':
    main(sys.argv[1])

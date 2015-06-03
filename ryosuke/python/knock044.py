# coding:utf-8
'''
python knock044.py ../Data/neko.txt.cabocha
'''

import sys
import knock041 as marujirou


def main(in_fname):
    doc = marujirou.create_doc(in_fname)
    print 'digraph dependency {'
    for sent_id, sent in enumerate(doc):
        for chunk_id, chunk in enumerate(sent):
            if chunk.dst != -1:
                print '%d.%d [label="%s"]' % (sent_id, chunk_id, chunk.get_raw())
                print '%d.%d -> %d.%d;' % (sent_id, chunk_id, sent_id, chunk.dst)
            elif chunk.srcs:
                print '%d.%d [label=%s]' % (sent_id, chunk_id, chunk.get_raw())
    print '}'

if __name__ == '__main__':
    main(sys.argv[1])

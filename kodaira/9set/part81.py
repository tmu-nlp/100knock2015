#!usr/bin/python

import bz2

coun_data = [tuple((count.strip(), count.strip().replace(' ', '_') ) ) \
    for count in open('country/countrys.txt').readlines()]

corpus = bz2.decompress(open('corpus.bz2', 'rb').read() )
corpus = corpus.replace('\n', ' ')
for before, after in coun_data:
    corpus = corpus.replace(before, after)
open('corpus2.bz2', 'w').write(bz2.compress(corpus, 9) )

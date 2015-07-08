#!usr/bin/python


import bz2
import re

open('corpus.bz2', 'w').write(\
    bz2.compress(
    re.sub(r'([!?,.;:\'\"\{\}\[\]\(\)]* [!?,.;:\'\"\{\}\[\]\(\)]*)+|([!?,.;:\'\"\{\}\[\]\(\)]+\n)', \
    lambda m: ' ' if not m.group(2) else ' \n', \
    bz2.decompress(open('enwiki.txt.bz2', 'rb').read() ) ), 9 ) )


#!usr/bin/python
#coding:utf-8

import re
import knock_40
import knock_41
from collections import defaultdict


if __name__ == "__main__":
    chunk_dict = defaultdict(list)
    chunk_list = knock_41.main(5)
    i = 0
    for chunks in chunk_list:
        for morph in chunks.morphs:
            chunk_dict[str(i)].append(morph.surface)
        i += 1

    for chunks in chunk_list:
        for morph in chunks.morphs:
            if morph.pos != u"補助記号":
                print morph.surface,
        print ("\t"),

        for j in chunk_dict[chunks.dst]:
            if j != u"。":
                print j,
        print ""



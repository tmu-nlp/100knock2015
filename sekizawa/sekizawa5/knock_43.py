#!usr/bin/python
#coding:utf-8

import knock_41
from collections import defaultdict

if __name__ == "__main__":
    chunk_dict = defaultdict(list)
    chunk_list = knock_41.main(5)
    i = 0
    for chunks in chunk_list:
        chunk_dict[str(i)].append(chunks.morphs)
        i += 1

    for chunks in chunk_list:
        flag = 0
        root_chunks = []
        dest_chunks = []
        for morph in chunks.morphs:
            if morph.pos == u"名詞" or morph.pos == u"代名詞":
                flag = 1

        for morph in chunks.morphs:
            if flag == 1 and morph.pos != u"補助記号":
                root_chunks.append(morph.surface)

        for morphs in chunk_dict[chunks.dst]:
            for morph in morphs:
                if morph.pos == u"動詞" and flag > 0:
                    flag = 2
            for morph in morphs:
                if flag == 2 and morph.pos != u"補助記号":
                    dest_chunks.append(morph.surface)
        if flag == 2:
            for root_chunk in root_chunks:
                print root_chunk,
            print "\t",
            for dest_chunk in dest_chunks:
                print dest_chunk,
            print ""



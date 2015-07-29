#!/usr/bin/python
# -*- coding:utf-8 -*-



from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst


def extr(sent_lst):
    for chunk_lst in sent_lst:
        for chunk in chunk_lst:
            if "名詞" in [m.pos for m in chunk.morphs] and\
               "動詞" in [m.pos for m in chunk_lst[chunk.dst].morphs]:
                src_text = "".join([m.surface for m in chunk.morphs
                                    if m.pos != "記号"])
                dst_text = "".join([m.surface for m in chunk_lst[chunk.dst].morphs
                                    if m.pos != "記号"])
                print src_text + "\t" + dst_text



if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr(sent_lst)

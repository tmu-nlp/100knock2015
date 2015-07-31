#!/usr/bin/python
# -*- coding:utf-8 -*-

from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst


def extr_case(sent_lst):
    for chunk_lst in sent_lst[5:6]:
        for chunk in chunk_lst:
            verbs = [m for m in chunk.morphs if m.pos == "動詞"]
            if len(verbs) >= 1:
                pred = verbs[0].base
                case_lst = []
                arg_lst = []
                for i in chunk.srcs:
                    morphs = [m for m in chunk_lst[i].morphs if m.pos != "記号"]
                    if len(morphs) >= 1 and morphs[-1].pos == "助詞":
                        case_lst.append(morphs[-1].base)
                        arg = "".join([m.surface for m in morphs])
                        arg_lst.append(arg)
                print "\t".join([pred, " ".join(case_lst), " ".join(arg_lst)])


if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr_case(sent_lst)





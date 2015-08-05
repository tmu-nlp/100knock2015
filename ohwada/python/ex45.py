#!/usr/bin/python
# -*- coding:utf-8 -*-

from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst


def extr_case(sent_lst):
    for chunk_lst in sent_lst:
        for chunk in chunk_lst:
            verbs = [m for m in chunk.morphs if m.pos == "動詞"]
            if len(verbs) >= 1:
                pred = verbs[0].base
                case_lst = []
                for i in chunk.srcs:
                    morphs = [m for m in chunk_lst[i].morphs if m.pos != "記号"]
                    if len(morphs) >= 1 and morphs[-1].pos == "助詞":
                        case_lst.append(morphs[-1].base)
                print pred + "\t" + " ".join(case_lst)


if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr_case(sent_lst)


# コマンド

# python ex45.py >case.txt

# 頻出する述語と格パターンの組み合わせ（上位N個）
# cat case.txt | sort | uniq -c | sort -k 1 -r | head -n N

# 「する」（「見る」「与える」）の格パターンを出現頻度順に
# cat case.txt | grep '^する\t' | sort | uniq -c | sort -k 1 -r

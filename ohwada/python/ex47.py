#!/usr/bin/python
# -*- coding:utf-8 -*-

from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst


def extr_case(sent_lst):
    for chunk_lst in sent_lst:
        for chunk in chunk_lst:
            verbs = [m for m in chunk.morphs if m.pos == "動詞"]
            if len(verbs) >= 1:
                verb = verbs[0].base
                pred = ""
                case_lst = []
                arg_lst = []
                for i in chunk.srcs:
                    morphs = [m for m in chunk_lst[i].morphs if m.pos != "記号"]
                    if len(morphs) >= 1 and morphs[-1].pos == "助詞":
                        if morphs[-1].surface == "を" and len(morphs) == 2 and\
                           morphs[0].pos1 == "サ変接続":
                            pred = "".join([m.surface for m in morphs]) + verb
                        else:    
                            case_lst.append(morphs[-1].base)
                            arg = "".join([m.surface for m in morphs])
                            arg_lst.append(arg)
                if pred != "":  
                    print "\t".join([pred, " ".join(case_lst), " ".join(arg_lst)])


if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr_case(sent_lst)


# コマンド

# python ex47.py >sahen.txt

# 上位N個
# 頻出する述語（"サ変+を+動詞"）
# cut -f 1 sahen.txt | sort | uniq -c | sort -k 1 -r | head -n N

# 頻出する述語と助詞パターン
# cut -f 1-2 sahen.txt | sort | uniq -c | sort -k 1 -r | head -n N 

#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from ex30 import read_mecab

def extr(sent_lst):
    A = ""
    for morph_lst in sent_lst:
        for dic in morph_lst:
            if dic["pos"] == "名詞":
                if A == "":
                    A = dic["surface"]
                else:
                    print A + "の" + dic["surface"]
                    A = ""
            elif dic["surface"] == "の":
                pass
            else:
                A = ""



if __name__ == "__main__":
    sent_lst = read_mecab("neko.txt.mecab")

    extr(sent_lst)

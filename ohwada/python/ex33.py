#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from ex30 import read_mecab

def extr(sent_lst):
    
    for morph_lst in sent_lst:
        for dic in morph_lst:
            if dic["pos"] == "名詞" and dic["pos1"] == "サ変接続":
                print dic["surface"]                 


if __name__ == "__main__":
    sent_lst = read_mecab("neko.txt.mecab")

    extr(sent_lst)

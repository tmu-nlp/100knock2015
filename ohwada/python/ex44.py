#!/usr/bin/python
# -*- coding:utf-8 -*-



from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst


def extr_tree(chunk_lst):
    with open("tree.dot", "w") as f:
        for chunk in chunk_lst:
            
        


if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr(sent_lst[0])

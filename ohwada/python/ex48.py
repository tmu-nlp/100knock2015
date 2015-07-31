#!/usr/bin/python
# -*- coding:utf-8 -*-

from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst


def get_path(chunk, chunk_lst):
    if chunk.dst is -1:
        return [chunk_lst[-1]]
    else:
        next_chunk = chunk_lst[chunk.dst]
        return [chunk] + get_path(next_chunk, chunk_lst)


def extr_paths(sent_lst):
    for chunk_lst in sent_lst:
        for chunk in chunk_lst:
            if chunk.is_np():
                path = get_path(chunk, chunk_lst)
                if len(path) > 1:
                    print " -> ".join([c.surface() for c in path])



if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr_paths(sent_lst)

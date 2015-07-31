#!/usr/bin/python
# -*- coding:utf-8 -*-


from ex40 import Morph
from ex41 import Chunk, sent_to_chunk_lst
from ex48 import get_path


def make_output(path, i, j, chunk_lst):
    lst = [chunk_lst.index(c) for c in path]
    if lst[0] is i:
        start = path[0].replace_np("X")
    elif lst[0] is j:
        start = path[0].replace_np("Y")
    if len(path) > 1 and lst[-1] is j:
        end = path[-1].replace_np("Y")
        return " -> ".join([start] + [c.surface() for c in path[1:-1]] + [end])
    else:
        return " -> ".join([start] + [c.surface() for c in path[1:]])


def extr_paths(sent_lst):
    for chunk_lst in sent_lst:
        nps = [c for c in chunk_lst if c.is_np()]
        for np in nps:
            path = get_path(np, chunk_lst)
            i = chunk_lst.index(np)
            nps_on_path = filter(lambda x:x in path, nps[nps.index(np)+1:])
            nps_not_on_path = filter(lambda x:x not in path, nps[nps.index(np)+1:])
            for np in nps_on_path:
                j = chunk_lst.index(np)
                print make_output(path[:path.index(np)+1], i, j, chunk_lst)
            for np in nps_not_on_path:
                other_path = get_path(np, chunk_lst)
                j = chunk_lst.index(np)
                for c in other_path:
                    if c in path:
                        output1 = make_output(path[:path.index(c)], i, j, chunk_lst)
                        output2 = make_output(other_path[:other_path.index(c)],
                                              i, j, chunk_lst)
                        print " | ".join([output1, output2, c.surface()])
                        break


if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_chunk_lst(f)
        extr_paths(sent_lst)

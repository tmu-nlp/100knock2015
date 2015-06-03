#!/usr/bin/python
#coding:utf-8
# 名詞を含む文節が動詞を含む文節にかかるものを抽出

from part41 import *
import pygraphviz as pgv

def draw_directed_graph(text_chunk_list):
    directed_graph = pgv.AGraph(strict = True, directed = True)
    count = 0
    for sentence_chunk_list in text_chunk_list:
        count += 1
        if count == 40:
            break
        for chunk in sentence_chunk_list:
            if chunk.dst != '-1':
                from_word = str(count) + ':' + chunk.get_phrase()
                to_word = str(count) + ':' + sentence_chunk_list[int(chunk.dst)].get_phrase()
                directed_graph.add_edge(from_word.decode('utf-8'), \
                        to_word.decode('utf-8'))

    directed_graph.layout()
    directed_graph.draw('directed_graph_by_pgv.png')


if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    draw_directed_graph(text_chunk_list)

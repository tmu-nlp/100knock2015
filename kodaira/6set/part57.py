#!usr/bin/python

import pygraphviz as pgv

def draw_directed_graph(xml_name):
    tag_collapsed = "<dependencies type=\"collapsed-dependencies\">"
    tag_collapsed_end = "</dependencies>"
    tag_governor = "</governor>"
    tag_dependent = "</dependent>"
    sentence_id = 0; sentence_num = ''
    collapsed_flag = False
    directed_graph = pgv.AGraph(strict = True, directed = True)
    for line in open(xml_name):
        if tag_collapsed in line:
            sentence_id += 1
            sentence_num = str(sentence_id) + "\t"
            collapsed_flag = True
        elif tag_collapsed_end in line:
            collapsed_flag = False
        elif collapsed_flag and tag_governor in line:
            governor = sentence_num + line.replace(tag_governor, '').split(">")[1]
        elif collapsed_flag and tag_dependent in line:
            dependent = sentence_num + line.replace(tag_dependent, '').split(">")[1]
            directed_graph.add_edge(dependent, governor)
    directed_graph.layout()
    directed_graph.draw('result_57.png')





if __name__ == "__main__":
    xml_name = "nlp.txt.xml"
    draw_directed_graph(xml_name)

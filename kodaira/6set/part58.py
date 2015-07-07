#!usr/bin/python

import pygraphviz as pgv
from collections import defaultdict

def choice_svo(xml_name):
    tag_collapsed = "<dependencies type=\"collapsed-dependencies\">"
    tag_collapsed_end = "</dependencies>"
    collapsed_flag = False;

    tag_governor = "</governor>"
    tag_dependent = "</dependent>"

    tag_dep = "<dep type=\""
    dep_type_flag = False 
    dep_type = ''
    dep_dict = defaultdict(lambda:  defaultdict(list) )

    sentence_id = 0; sentence_num = ''

    for line in open(xml_name):
        if tag_collapsed in line:
            sentence_id += 1
            sentence_num = str(sentence_id) + "\t"
            collapsed_flag = True
            dep_dict = defaultdict(lambda:  defaultdict(list) )
        if collapsed_flag:
            if tag_collapsed_end in line:
                make_svo(dep_dict)
                collapsed_flag = False
                
            if tag_dep in line:
                dep_type = line.replace(tag_dep, '').strip().split("\"")[0]
                if dep_type == "dobj" or dep_type == "nsubj":
                    dep_type_flag = True
                else:
                    dep_type_flag = False
            if dep_type_flag:
                if tag_governor in line:
                    governor = line.replace(tag_governor, '').strip().split(">")[1]
                elif tag_dependent in line:
                    dependent = line.replace(tag_dependent, '').strip().split(">")[1]
                    dep_dict[dep_type][governor].append(dependent)


def make_svo(dep_dict):
    predicate_list = list()
    for governor_word in dep_dict["nsubj"]:
        if governor_word in dep_dict["dobj"]:
            predicate_list.append(governor_word)
    subject_list = list()
    object_list = list()
    for predicate in predicate_list:
        print "\t".join((",".join(dep_dict["nsubj"][predicate]), predicate, ",".join(dep_dict["dobj"][predicate]) )) 
        


if __name__ == "__main__":
    xml_name = "nlp.txt.xml"
    choice_svo(xml_name)

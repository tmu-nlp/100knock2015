#!usr/bin/python
#coding=utf-8


from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et

from collections import defaultdict
def print_svo(deps):
    nsubj_dict = defaultdict(list); dobj_dict = defaultdict(list)
    # make dict 
    for dep in deps:
        dep_type = dep['type']
        if dep_type == 'dobj':
            nsubj_dict[dep.governor.renderContents()] \
                = dep.dependent.renderContents()
        elif dep_type == 'nsubj':
            dobj_dict[dep.governor.renderContents()] \
                = dep.dependent.renderContents()
    # print SVO
    for governor in nsubj_dict.keys():
        if governor in dobj_dict:
            print '\t'.join((nsubj_dict[governor], governor, dobj_dict[governor]))


def tuple_extraction(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    
    dependencies_list = xml_soup('dependencies')
    for dependencies in dependencies_list:
        if dependencies['type'] == 'collapsed-dependencies':
            print_svo(dependencies('dep') )
                



if __name__ == '__main__':

    xml_name = 'nlp.txt.xml'
    tuple_extraction(xml_name)

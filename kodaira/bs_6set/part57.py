#!usr/bin/python
#coding=utf-8


from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et

import pygraphviz as pgv

def draw_directed_graph(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    
    dependencies_list = xml_soup('dependencies')
    count = 0
    directed_graph = pgv.AGraph(strict = False, directed = True)
    for dependencies in dependencies_list:
        count += 1
        tag = str(count)
        if dependencies['type'] == 'collapsed-dependencies':
            for dep in dependencies('dep'):
               directed_graph.add_edge(tag + dep.governor.renderContents(), \
                    tag + dep.dependent.renderContents() )

            directed_graph.layout()
    directed_graph.draw('result_57.png')
             
                



if __name__ == '__main__':

    xml_name = 'nlp.txt.xml'
    draw_directed_graph(xml_name)

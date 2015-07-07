# coding:utf-8
'''
python knock059.py ../Data/nlp.txt.xml
'''

import sys
import re
import xml.sax as sax

class Node:
    def __init__(self, tag, parent, word=None):
        self.tag = tag
        self.parent = parent
        self.word = word
        self.children = list()

class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.current_tag = ''

    def startElement(self, name, attrs):
        self.current_tag = name

    def characters(self, content):
        if self.current_tag == 'parse':
            for np in self.get_nps(content.strip()):
                print np
        
    def endElement(self, name):
        self.current_tag = ''

    def get_nps(self, s_expression):
        root = self.make_tree(s_expression)
        for node in self.walk_depth_first(root):
            if node.tag == 'NP':
                yield self.get_terminals(node)

    def walk_depth_first(self, node):
        stack = [node]
        while stack:
            current = stack.pop(0)
            yield current
            stack = current.children + stack
       
    def get_terminals(self, node):
        words = list()
        stack = [node]
        for current in self.walk_depth_first(node):
            if current.word:
                words.append(current.word)
        return ' '.join(words)

    def make_tree(self, s_expression):
        current_node = Node('out of root', None)
        for i in range(len(s_expression)):
            if s_expression[i] == '(':
                word = None
                if not s_expression[i+1:].split()[1].startswith('('):
                    word = s_expression[i+1:].split()[1].split(')')[0]
                tag = s_expression[i+1:].split()[0]
                child = Node(tag, current_node, word)
                current_node.children.append(child)
                current_node = child
                continue
            if s_expression[i] == ')':
                current_node = current_node.parent 
        return current_node

def main(in_fname):
    parser = sax.make_parser()
    parser.setContentHandler(StanfordCoreXMLHandler())
    parser.parse(open(in_fname))

if __name__ == '__main__':
    main(sys.argv[1])

#!usr/bin/python
#coding=utf-8


from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et

from collections import defaultdict

def print_person(token):
    if token.ner.renderContents() == 'PERSON':
        print token.word.renderContents()
def coreference_ana(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    
    tokens = xml_soup('token')
    for token in tokens:
        print_person(token)

if __name__ == '__main__':

    xml_name = 'nlp.txt.xml'
    coreference_ana(xml_name)

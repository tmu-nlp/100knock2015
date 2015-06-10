#!usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et


def print_content(token):
    content = '単語；' + token.word.renderContents()
    content += '\tレンマ：' + token.lemma.renderContents()
    content += '\t品詞：' + token.lemma.renderContents()
    print content


def add_tag(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    tokens = xml_soup('token')
    for token in tokens:
        print_content(token)



if __name__ == '__main__':
    xml_name = 'nlp.txt.xml'
    add_tag(xml_name)

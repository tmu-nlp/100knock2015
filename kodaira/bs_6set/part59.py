#!usr/bin/python
#coding=utf-8


from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et

from collections import defaultdict


def tuple_extraction(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    
    for parse in xml_soup('parse'):
        word_list = parse.renderContents().split(" ")
        for begin in range(len(word_list) ):
            if "(NP" in word_list[begin]:
                count = 1
                for num in range(begin + 1, len(word_list) ):
                    word = word_list[num]
                    if "(" in word:
                        count += 1
                    elif ")" in word:
                        count -= word.count(")")
                        print word.replace(")", ''),
                    if count < 1:
                        break;
                print ''
        print ''


if __name__ == '__main__':

    xml_name = 'nlp.txt.xml'
    tuple_extraction(xml_name)

#!usr/bin/python


from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et



def tokenization(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    words = xml_soup('word')
    for word in words:
        print word.renderContents()



if __name__ == '__main__':
    xml_name = 'nlp.txt.xml'
    tokenization(xml_name)

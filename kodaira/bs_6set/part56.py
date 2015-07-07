#!usr/bin/python
#coding=utf-8


from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et

from collections import defaultdict

def print_person(token):
    if token.ner.renderContents() == 'PERSON':
        print token.word.renderContents()


tag_end = '<end>'; tag_start = '<start>'; tag_mention = '<mention>'
def add_mention_info(mention_dict, mention, representative_words):
    mention_dict[tag_end].append(mention.end.renderContents() )
    mention_dict[tag_start].append(mention.start.renderContents() )
    mention_dict[tag_mention].append(representative_words)


def get_coreference_dict(coreferences):
    mention_dict = defaultdict(lambda: defaultdict(list) )
    for coreference in coreferences:
        for mention in coreference('mention'):
            if mention.get('representative', {}):
                print mention
                representative_words = mention.find('text').renderContents()
            else:
                add_mention_info \
                    (mention_dict[mention.sentence.renderContents()] \
                    , mention, representative_words)
    return mention_dict
 
def get_parenthesis(coreference_dict, token_id):
    parenthesis = ''
    if token_id in coreference_dict[tag_start]:
        parenthesis = '[' + coreference_dict[tag_mention][0] + '('
    if token_id in coreference_dict[tag_end]:
        for num in range(coreference_dict[tag_end].count(token_id) - 1):
            parenthesis += ') ] '
    return parenthesis


def coreference_ana(xml_name):
    xml_soup = BeautifulSoup(open(xml_name) )
    
    coreferences = xml_soup('coreference')
    coreference_dict = get_coreference_dict(coreferences)
    sentences = xml_soup('sentence')
    for sentence in sentences:
        sentence_id = sentence.get('id', 0)
        if not sentence_id:
           continue
        for token in sentence.findAll('token'):
            token_id = token['id']
            if sentence_id in coreference_dict:

                parenthesis = get_parenthesis \
                    (coreference_dict[sentence_id], token_id)
            else:
                parenthesis = ''
            print parenthesis + token.word.renderContents(),
        print         
 


if __name__ == '__main__':

    xml_name = 'nlp.txt.xml'
    coreference_ana(xml_name)

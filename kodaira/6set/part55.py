#!usr/bin/python

from part53 import *

def named_entity_extraction(file_name):
    tag_word = "<word>"; person = "PERSON"
    word = ''
    for line in open(file_name):
        if tag_word in line:
            word = get_content_tags(line, tag_word)
        elif person in line:
            print word



if __name__ == "__main__":
    file_name = "nlp.txt.xml"
    named_entity_extraction(file_name)

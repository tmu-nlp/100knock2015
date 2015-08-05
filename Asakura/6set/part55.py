#!usr/bin/python
#coding:utf-8

import re

def main():
    re_pattern = re.compile('<word>(.+?)</word>')
    re_check = re.compile('<NER>PERSON</NER>')
    person_list = list()
    for line in open('nlp.txt.xml'):
        word_result = re_pattern.search(line)
        ner_result = re_check.search(line)
        if word_result is not None:
            word = word_result.group(1)
        if ner_result is not None:
            person_list.append(word)
    for name in person_list:
        print name

if __name__ == '__main__':
    main()

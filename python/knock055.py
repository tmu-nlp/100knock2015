# coding:utf-8
'''
python knock055.py ../Data/nlp.txt.xml
'''

import sys
import xml.sax as sax


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = ['root']

    def startElement(self, name, attrs):
        self.push_tag(name)

    def characters(self, content):
        if self.get_current_tag() == 'word':
            self.current_word = content
        if self.get_current_tag() == 'NER' and content == 'PERSON':
            print self.current_word
            
    def endElement(self, name):
        self.pop_tag()

    def get_current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)
    

def main(in_fname):
       parser = sax.make_parser()
       parser.setContentHandler(StanfordCoreXMLHandler())
       parser.parse(open(in_fname))

if __name__ == '__main__':
    main(sys.argv[1])

#!/usr/bin/python
# coding:utf-8

import sys
import xml.sax as sax

class Coreference():
    def __init__(self, representative):
        self.representative = representative
        self.sentence_id = None
        self.start = None
        self.end = None

    def __str__(self):
        return '%s, %d, %d, %d' % (self.representative, self.sentence_id, self.start, self.end)

class CoreferenceHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = []
        self.coreferencese = []
        self.current_coref = None
        self.representative = False
        self.current_rep = ''

    def startElement(self, name, attrs):
        self.push_tag(name)
        if name == 'mention' and 'representative' in attrs:
            self.representative = True
        elif name == 'mention':
            self.representative = False

    def characters(self, content):
        if self.isIn('mention') and not self.representative:
            if self.get_current_tag() == 'sentence':
                self.current_coref = Coreference(self.current_rep)
                self.current_coref.sentence_id = int(content)
            if self.get_current_tag() == 'start':
                self.current_coref.start = int(content)
            if self.get_current_tag() == 'end':
                self.current_coref.end = int(content)

        if self.representative and self.get_current_tag() == 'text':
            self.current_rep = content.encode('utf-8')

    def endElement(self, name):
        self.pop_tag()
        if name == 'mention' and not self.representative:
            self.coreferencese.append(self.current_coref)

    def get_current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)

    def isIn(self, name):
        return name in self.tags


class PrintHandler(sax.handler.ContentHandler):
    def __init__(self, coreferencese):
        self.tags = []
        self.coreferencese = coreferencese 
        self.sent = []

    def startElement(self, name, attrs):
        self.push_tag(name)
        if name == 'sentence' and self.isIn('sentences'):
            self.targets = [coref for coref in self.coreferencese if coref.sentence_id == int(attrs['id'])]

    def characters(self, content):
        if self.get_current_tag() == 'word':
            self.sent.append(content.encode('utf-8'))

    def endElement(self, name):
        self.pop_tag()
        if name == 'sentence' and self.isIn('sentences'):
            for coref in sorted(self.targets, key=lambda x: -x.start):
                self.sent.insert(coref.end-1, '」')
                self.sent.insert(coref.end-1, ')')
                self.sent.insert(coref.start-1, '(')
                for tok in coref.representative.split(' '):
                    self.sent.insert(coref.start-1, tok)
                self.sent.insert(coref.start-1, '「')
            print ' '.join(self.sent)
            self.sent = []

    def get_current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)

    def isIn(self, name):
        return name in self.tags

def main(in_fname):
    # get coreference lists 
    coref_handler = CoreferenceHandler()
    parser = sax.make_parser()
    parser.setContentHandler(coref_handler)
    parser.parse(open(in_fname))

    # outputs
    print_handler = PrintHandler(coref_handler.coreferencese)
    parser.setContentHandler(print_handler)
    parser.parse(open(in_fname))

if __name__ == '__main__':
    main(sys.argv[1])
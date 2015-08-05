#!/usr/bin/python
# coding:utf-8
#固有表現抽出。入力文中の人名を全て
import sys
import xml.sax as sax


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = []

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
       parser = sax.make_parser()#SAX XML Reader オブジェクトを作成して返す。パーサには最初に見つかったものが使われる
       parser.setContentHandler(StanfordCoreXMLHandler())#StanfordCoreXMLHandlerをセットする
       parser.parse(open(in_fname))#

if __name__ == '__main__':
    main(sys.argv[1])
# coding:utf-8
'''
python knock057.py ../Data/nlp.txt.xml
'''

import sys
import xml.sax as sax


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = []
        self.sent_id = 0
        self.dpend_flag = False
        self.current_type = ''
        self.gov_id = 0
        self.dep_id = 0

    def startElement(self, name, attrs):
        self.push_tag(name)
        if name == 'sentence' and 'id' in attrs:
            self.sent_id = int(attrs['id'])
        if name == 'dependencies' and 'type' in attrs:
            if attrs['type'] == 'collapsed-dependencies':
                self.dpend_flag = True
        if self.dpend_flag and name == 'dep':
            self.current_type = attrs['type'].encode('utf-8')
        if self.dpend_flag and name == 'governor':
            self.gov_id = int(attrs['idx'])
        if self.dpend_flag and name == 'dependent':
            self.dep_id = int(attrs['idx'])

    def characters(self, content):
        if self.dpend_flag:
            if self.get_current_tag() == 'governor':
                print '%d.%d [label="%s"]' % (self.sent_id, self.gov_id, content)
            if self.get_current_tag() == 'dependent':
                print '%d.%d [label="%s"]' % (self.sent_id, self.dep_id, content)
                print '%d.%d -> %d.%d [label="%s"];' % (self.sent_id, self.gov_id, self.sent_id, self.dep_id, self.current_type)
            
    def endElement(self, name):
        self.pop_tag()
        if name == 'dependencies':
                self.dpend_flag = False

    def get_current_tag(self):
        return self.tags[-1]

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)
    
    def isIn(self, tag):
        return tag in self.tags

def main(in_fname):
    print 'digraph collapsed_dependencies {'
    parser = sax.make_parser()
    parser.setContentHandler(StanfordCoreXMLHandler())
    parser.parse(open(in_fname))
    print '}'

if __name__ == '__main__':
    main(sys.argv[1])

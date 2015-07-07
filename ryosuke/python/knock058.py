# coding:utf-8
'''
python knock059.py ../Data/nlp.txt.xml
'''

import sys
import xml.sax as sax


class StanfordCoreXMLHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.tags = []
        self.dpend_flag = False
        self.current_type = ''
        self.candidate = list()
        self.id2word = dict()
        self.gov_id = None
        self.dep_id = None
        self.result = list()

    def startElement(self, name, attrs):
        self.push_tag(name)
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
                self.id2word[self.gov_id] = content
            if self.get_current_tag() == 'dependent':
                self.id2word[self.dep_id] = content
            
    def endElement(self, name):
        self.pop_tag()
        if name == 'dependencies':
            self.dpend_flag = False
            for pred, subj, obj in self.result:
                print '\t'.join([pred, subj, obj])
#                print pred, subj, obj
            self.id2word = dict()
            self.candidate = list()
            self.result = list()

        if name == 'dep' and self.dpend_flag:
            if self.current_type == 'nsubj':
                self.candidate_update((self.gov_id, self.dep_id, None))
            if self.current_type == 'dobj':
                self.candidate_update((self.gov_id, None, self.dep_id))


    def get_current_tag(self):
        return self.tags[-1]

    def candidate_update(self, tupl):
        if tupl[2] is None:
            for t in self.candidate:
                if t[1] is None and t[0] == tupl[0] and t[2] is not None:
                    self.candidate.remove(t)
                    self.result.append((self.id2word[t[0]], self.id2word[tupl[1]], self.id2word[t[2]]))
#                    self.result.append((t[0], tupl[1], t[2]))
                    break
            else:
                self.candidate.append(tupl)
        if tupl[1] is None:
            for t in self.candidate:
                if t[2] is None and t[0] == tupl[0] and t[1] is not None:
                    self.candidate.remove(t)
                    self.result.append((self.id2word[t[0]], self.id2word[t[1]], self.id2word[tupl[2]]))
#                    self.result.append((t[0], t[1], tupl[2]))
                    break
            else:
                self.candidate.append(tupl)
#        print tupl
#        if tupl[1] is None:
#            print self.id2word[tupl[0]], 'None', self.id2word[tupl[2]]
#        else:
#            print self.id2word[tupl[0]], self.id2word[tupl[1]], 'None'
#
#        print self.candidate
#        print self.result

    def push_tag(self, tag):
        self.tags.append(tag)

    def pop_tag(self):
        return self.tags.pop(-1)
    
    def isIn(self, tag):
        return tag in self.tags

def main(in_fname):
    parser = sax.make_parser()
    parser.setContentHandler(StanfordCoreXMLHandler())
    parser.parse(open(in_fname))

if __name__ == '__main__':
    main(sys.argv[1])

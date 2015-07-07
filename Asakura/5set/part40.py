#!usr/bin/python
#--*--coding:utf-8--*--

class Morph(object):
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def make_morph(cabocha_file):
    all_sent = []#文書の構文解析結果が格納されている
    one_sent = []#1文の構文解析結果が格納されている
    for line in open(cabocha_file):
        if '\t' in line:
            surf, item = line.strip().split('\t')
            items = item.split(',')
            morph = Morph(surf,items[6],items[0],items[1])
            one_sent.append(morph)
        elif 'EOS' in line:
            if one_sent:
                all_sent.append(one_sent)
                one_sent = []
    for item in all_sent[2]:
        print 'surface = %s\tbase=%s\tpos=%s\tpos1=%s' %\
                (item.surface,item.base,item.pos,item.pos1)
if __name__ == '__main__':
    make_morph('neko.cabocha')

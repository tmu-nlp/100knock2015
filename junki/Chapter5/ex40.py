#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def main():
    doc = list()
    sent = list()
    for line in open(sys.argv[1],'r'):
        if line == "EOS\n":
            doc.append(sent)
            sent = list()
            continue
        elif len(line.split("\t")) < 2:#line.startswith('EOS'):
            continue
        morph = {}
        surface, items = line.strip().split("\t")
        item_list = items.split(",")
        sent.append(Morph(surface,item_list[6],item_list[0],item_list[1]))
    return doc


if __name__ == '__main__':
    my_morphs = main()
    count = 0
    for kei in my_morphs:
        count += 1
        for kei2 in kei:
            if count == 3:
                print kei2.surface
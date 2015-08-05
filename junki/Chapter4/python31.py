#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

def main():
    doc = list()
    sent = list()
    for line in open(sys.argv[1],'r'):
        if len(line.split("\t")) < 2:#line.startswith('EOS'):
            #if sent: 
            doc.append(sent)
            sent = list()
            continue
        morph = {}
        surface, items = line.strip().split("\t")
        item_list = items.split(",")
        morph['surface'] = surface
        morph['base'] = item_list[6]
        morph['pos'] = item_list[0]
        morph['pos1'] = item_list[1]
        sent.append(morph)
    return doc


if __name__ == '__main__':
    my_morphs = main()
    for kei in my_morphs:
        for kei2 in kei:
        	if '動詞' == kei2['pos'] :
        		print kei2['surface'] 
#!/usr/bin/python
#_*_coding:utf-8_*_


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


if __name__ == "__main__":

    input_file = open("neko.txt.cabocha", "r")
    sentense_list = []
    all_list = []

    for line in input_file:
        if "\t" in line:
            key, items = line.strip().split("\t")
            item = items.split(",")
            morph = Morph(key, item[6], item[0], item[1])
            sentense_list.append(morph)
        #実際のファイルの2文目に空の文字列があるから
        #この空の文字列をsentense_listに入れないようにする工夫が必要
        #ここは何をしている？
        elif "EOS" in line:
            if sentense_list:
                all_list.append(sentense_list)
                sentense_list = []

    for morph in all_list[1]:
        print "surface: %s, base: %s, pos: %s, pos1: %s" % \
            (morph.surface, morph.base, morph.pos, morph.pos1)

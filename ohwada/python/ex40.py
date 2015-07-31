#!/usr/bin/python
# -*- coding:utf-8 -*-


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def sent_to_morph_lst(cabocha_file):

    sent_lst = []
    morph_lst = []
    for line in cabocha_file:
        line = line.strip()
        if line[:2] == "* ":
            pass
        elif line == "EOS":
            if len(morph_lst) != 0:
                sent_lst.append(morph_lst)
                morph_lst = []
        else:
            (surface, features) = line.split("\t")
            features = features.split(",")
            (base, pos, pos1) = (features[6], features[0], features[1])
            morph_lst.append(Morph(surface, base, pos, pos1))


    return sent_lst

if __name__ == "__main__":
    with open("neko.txt.cabocha", "r") as f:
        sent_lst = sent_to_morph_lst(f)

    for morph in sent_lst[2]:
        print morph.surface    
        

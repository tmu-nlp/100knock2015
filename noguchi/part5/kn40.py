# coding: utf-8

import sys


class Morph:
    """docstring for Morph"""
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def make_morph_class(fin):
    one_sent_list = list()
    all_sent_list = list()

    for line in fin:
        line = line.strip()
        if "* " not in line:
            if line != "EOS":
                surface, morph = line.split("\t")
                morph_list = morph.split(",")
                base, pos, pos1 = (morph_list[6], morph_list[0], morph_list[1])
                one_sent_list.append(Morph(surface, base, pos, pos1))

            else:
                all_sent_list.append(one_sent_list)
                one_sent_list = list()
    return all_sent_list


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = make_morph_class(fin)
    fin.close()
    for morph in all_sent_list[2]:
        print "\t".join((morph.surface, morph.base, morph.pos, morph.pos1))


if __name__ == "__main__":
    main()

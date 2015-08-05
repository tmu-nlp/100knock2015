#!/usr/bin/python
#_*_coding:utf-8_*_


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = list(morphs)
        self.dst = dst
        self.srcs = list(srcs)

    def srcs():
        pass
        #ここから始める


def make_morph(input_file):
    sentence_list = []
    all_list = []

    for line in input_file:
        if "\t" in line:
            key, items = line.strip().split("\t")
            item = items.split(",")
            morph = Morph(key, item[6], item[0], item[1])
            #そもそもクラスとは何ぞや？といことが理解できてない・・・？k
            sentence_list.append(morph)

        elif "EOS" in line:
            if sentence_list:
                all_list.append(sentence_list)
                sentence_list = []

    return all_list


def make_chunk(input_file, morph_list):
    sentence_list = []
    all_list = []

    for line in input_file:
        if "* " in line:
            line = line.replace("D", "")
            words = line.strip().split(" ")
            #係り受け先(srcs)って何？
            #* 2 -1
            chunk = Chunk(morph_list, words[2], words[2])
            sentence_list.append(chunk)

        elif "EOS" in line:
            if sentence_list:
                all_list.append(sentence_list)
                sentence_list = []

    return all_list


def main():
    input_file = open("neko.txt.cabocha", "r")
    morph_list = make_morph(input_file)
    input_file.seek(0)
    chunk_list = make_chunk(input_file, morph_list)
    input_file.close()
    for chunk in chunk_list[2]:
        print "文字列: %s, 係り受け先: %s" % (chunk.morph, chunk.dst)


if __name__ == "__main__":
    main()

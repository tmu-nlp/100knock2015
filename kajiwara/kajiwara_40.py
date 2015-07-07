# coding:utf-8


class Morph:
    def __init__(self, line):
        surface, features = line.strip().split("\t")
        features = features.split(",")
        self.surface = surface
        self.base = features[6]
        self.pos = features[0]
        self.pos1 = features[1]


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha", "r")
    sentence = list()
    sentences = list()
    for line in fin:
        if line.startswith("* "):
            continue
        elif line == "EOS\n":
            sentences.append(sentence)
            sentence = list()
        else:
            sentence.append(Morph(line))
    fin.close()
    print " ".join([morph.surface for morph in sentences[2]])


if __name__ == '__main__':
    main()

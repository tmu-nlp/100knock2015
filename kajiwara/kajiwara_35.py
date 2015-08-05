# coding:utf-8

import kajiwara_30 as mogura


def get_compound_nouns(morph_lists):
    compound_nouns = list()
    for morph_list in morph_lists:
        compound_noun = ""
        for morph_dict in morph_list:
            if morph_dict["pos"] == "名詞":
                compound_noun += morph_dict["surface"]
                continue
            if not compound_noun:
                continue
            compound_nouns.append(compound_noun)
            compound_noun = ""
    return compound_nouns


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    compound_nouns = get_compound_nouns(morph_lists)
    for compound_noun in compound_nouns:
        print compound_noun


if __name__ == '__main__':
    main()

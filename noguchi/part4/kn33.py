# coding: utf-8

import kn30 as senbei


def search_sahen_noun(morph_map, sahen_noun_list):
    if morph_map["pos"] == "名詞" and morph_map["pos1"] == "サ変接続":
        sahen_noun = morph_map["surface"]
        sahen_noun_list.append(sahen_noun)


def make_sahen_noun_list(morph_mapping_lists):
    sahen_noun_list = list()
    for morph_mapping_list in morph_mapping_lists:
        for morph_map in morph_mapping_list:
            search_sahen_noun(morph_map, sahen_noun_list)
    return sahen_noun_list


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    sahen_noun_list = make_sahen_noun_list(morph_mapping_lists)
    for sahen_noun in sahen_noun_list:
        print sahen_noun


if __name__ == "__main__":
    main()

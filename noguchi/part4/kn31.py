# coding: utf-8

import kn30 as senbei


def search_verb(morph_map, verb_list):
    if morph_map["pos"] == "動詞":
        verb = morph_map["surface"]
        verb_list.append(verb)


def make_verb_list(morph_mapping_lists):
    verb_list = list()
    for morph_mapping_list in morph_mapping_lists:
        for morph_map in morph_mapping_list:
            search_verb(morph_map, verb_list)
    return verb_list


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    verb_list = make_verb_list(morph_mapping_lists)
    for verb in verb_list:
        print verb


if __name__ == "__main__":
    main()

# coding: utf-8

import kn30 as senbei


def search_verb_base(morph_map, verb_base_list):
    if morph_map["pos"] == "動詞":
        verb_base = morph_map["base"]
        verb_base_list.append(verb_base)


def make_verb_base_list(morph_mapping_lists):
    verb_base_list = list()
    for morph_mapping_list in morph_mapping_lists:
        for morph_map in morph_mapping_list:
            search_verb_base(morph_map, verb_base_list)
    return verb_base_list


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    verb_base_list = make_verb_base_list(morph_mapping_lists)
    for verb_base in verb_base_list:
        print verb_base


if __name__ == "__main__":
    main()

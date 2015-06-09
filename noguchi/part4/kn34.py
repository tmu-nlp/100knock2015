# coding: utf-8

import kn30 as senbei


def search_no_noun_phrase(morph_mapping_list_trigram, no_noun_phrase_list):
    morph_map_1 = morph_mapping_list_trigram[0]
    morph_map_2 = morph_mapping_list_trigram[1]
    morph_map_3 = morph_mapping_list_trigram[2]
    if morph_map_1["pos"] == "名詞" and morph_map_2["surface"] == "の" and morph_map_3["pos"] == "名詞":
        no_noun_phrase = morph_map_1["surface"] + morph_map_2["surface"] + morph_map_3["surface"]
        no_noun_phrase_list.append(no_noun_phrase)


def make_no_noun_phrase_list(morph_mapping_lists):
    no_noun_phrase_list = list()
    for morph_mapping_list in morph_mapping_lists:
        for i in range(len(morph_mapping_list) - 2):
            morph_mapping_list_trigram = morph_mapping_list[i:i + 3]
            search_no_noun_phrase(morph_mapping_list_trigram, no_noun_phrase_list)
    return no_noun_phrase_list


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    no_noun_phrase_list = make_no_noun_phrase_list(morph_mapping_lists)
    for no_noun_phrase in no_noun_phrase_list:
        print no_noun_phrase


if __name__ == "__main__":
    main()

# coding: utf-8

import kn30 as senbei


def search_noun_rensetsu(morph_mapping_list_bigram, noun_rensetsu_list):
    morph_map_1 = morph_mapping_list_bigram[0]
    morph_map_2 = morph_mapping_list_bigram[1]
    if morph_map_1["pos"] == "名詞" and morph_map_2["pos"] == "名詞":
        noun_rensetsu = morph_map_1["surface"] + morph_map_2["surface"]
        noun_rensetsu_list.append(noun_rensetsu)


def make_noun_rensetsu_list(morph_mapping_lists):
    noun_rensetsu_list = list()
    for morph_mapping_list in morph_mapping_lists:
        for i in range(len(morph_mapping_list) - 1):
            morph_mapping_list_bigram = morph_mapping_list[i:i + 2]
            search_noun_rensetsu(morph_mapping_list_bigram, noun_rensetsu_list)
    return noun_rensetsu_list


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = senbei.make_morph_mapping_lists(fin)
    fin.close()
    noun_rensetsu_list = make_noun_rensetsu_list(morph_mapping_lists)
    for noun_rensetsu in noun_rensetsu_list:
        print noun_rensetsu


if __name__ == "__main__":
    main()

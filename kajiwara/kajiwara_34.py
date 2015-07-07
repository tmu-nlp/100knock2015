# coding:utf-8

import kajiwara_30 as mogura
import kajiwara_05 as mogram


def get_tri_gram(morph_lists):
    tri_grams = list()
    for morph_list in morph_lists:
        tri_grams.extend(mogram.n_gram(morph_list, 3))
    return tri_grams


def get_noun_phrases(tri_grams):
    noun_phrases = list()
    for tri_gram in tri_grams:
        if tri_gram[0]["pos"] == "名詞" and tri_gram[1]["surface"] == "の" and tri_gram[2]["pos"] == "名詞":
            noun_phrases.append("".join([morph_dict["surface"] for morph_dict in tri_gram]))
    return noun_phrases


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    tri_grams = get_tri_gram(morph_lists)
    noun_phrases = get_noun_phrases(tri_grams)
    for noun_phrase in noun_phrases[:5]:
        print noun_phrase


if __name__ == '__main__':
    main()

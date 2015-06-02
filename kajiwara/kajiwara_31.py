# coding:utf-8

import kajiwara_30 as mogura


def get_verbs(morph_lists):
    return [morph_dict["surface"] for morph_list in morph_lists for morph_dict in morph_list if morph_dict["pos"] == "動詞"]


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = mogura.get_morphs(fin)
    fin.close()
    verbs = get_verbs(morph_lists)
    print len(verbs)
    print ", ".join(verbs[:10])


if __name__ == '__main__':
    main()

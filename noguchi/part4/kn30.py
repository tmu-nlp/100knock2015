# coding: utf-8


def make_morph_mapping_lists(fin):
    morph_mapping_list = list()
    morph_mapping_lists = list()
    for line in fin:
        line = line.strip()
        if line != "EOS":
            surface, morph = line.strip().split("\t")
            morph_list = morph.split(",")
            pos, pos1, base = (morph_list[0], morph_list[1], morph_list[6])
            morph_map = {"surface": surface, "pos": pos, "pos1": pos1, "base": base}
            morph_mapping_list.append(morph_map)
        else:
            morph_mapping_lists.append(morph_mapping_list)
            morph_mapping_list = list()
    return morph_mapping_lists


def print_morph_mapping_list(morph_mapping_list):
    for morph_map in morph_mapping_list:
        print "表層形: " + morph_map["surface"] + \
              "\t基本形: " + morph_map["base"] + \
              "\t品詞: " + morph_map["pos"] + \
              "\t品詞細分類: " + morph_map["pos1"]


def print_morph_mapping_lists(morph_mapping_lists):
    for morph_mapping_list in morph_mapping_lists:
        print_morph_mapping_list(morph_mapping_list)


def main():
    fin = open("neko.txt.mecab", "r")
    morph_mapping_lists = make_morph_mapping_lists(fin)
    fin.close()
    print_morph_mapping_lists(morph_mapping_lists)


if __name__ == "__main__":
    main()

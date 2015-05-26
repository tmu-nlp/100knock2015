# coding:utf-8


def get_morphs(fin):
    morph_lists = list()
    morph_list = list()
    for line in fin:
        line = line.strip()
        if line == "EOS":
            morph_lists.append(morph_list)
            morph_list = list()
            continue
        surface, features = line.split("\t")
        try:
            pos, pos1, pos2, pos3, conju1, conju2, base, pronun1, pronun2 = features.split(",")
        except:
            pos, pos1, pos2, pos3, conju1, conju2, base = features.split(",")
            pronun1, pronun2 = ("*", "*")
        morph_list.append({"surface": surface, "base": base, "pos": pos, "pos1": pos1})
    return morph_lists


def main():
    fin = open("/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.mecab", "r")
    morph_lists = get_morphs(fin)
    fin.close()
    for morph_list in morph_lists:
        for morph_dict in morph_list:
            print "表層形：", morph_dict["surface"]
            print "原形：　", morph_dict["base"]
            print "品詞：　", morph_dict["pos"]
            print "品詞１：", morph_dict["pos1"]
            print ""


if __name__ == '__main__':
    main()

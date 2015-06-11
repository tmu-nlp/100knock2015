# coding: utf-8

import sys
import kn41 as chunk_senbei


def make_kakariuke_list(all_sent_list):
    kakariuke_list = list()
    for one_sent_list in all_sent_list:
        kakariuke_num_list = list()
        count = 0
        for chunk in one_sent_list:
            noun_flag, verb_flag = (False, False)
            if chunk.dst != str(-1):
                morph_kakarimoto = one_sent_list[count].morphs
                kakariuke_kakarimoto_list = list()
                for morph in morph_kakarimoto:
                    if morph.pos != "記号":
                        kakariuke_kakarimoto_list.append(morph.surface)
                    if morph.pos == "名詞":
                        noun_flag = True
                kakariuke_kakarimoto = "".join(kakariuke_kakarimoto_list)
                morph_kakarisaki = one_sent_list[int(chunk.dst)].morphs
                kakariuke_kakarisaki_list = list()
                for morph in morph_kakarisaki:
                    if morph.pos != "記号":
                        kakariuke_kakarisaki_list.append(morph.surface)
                    if morph.pos == "動詞":
                        verb_flag = True
                kakariuke_kakarisaki = "".join(kakariuke_kakarisaki_list)
                if noun_flag and verb_flag:
                    kakariuke_list.append((kakariuke_kakarimoto, kakariuke_kakarisaki))
            count += 1
    return kakariuke_list


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = chunk_senbei.make_chunk_class(fin)
    fin.close()
    kakariuke_list = make_kakariuke_list(all_sent_list)
    for kakariuke in kakariuke_list:
        print kakariuke[0] + "\t" + kakariuke[1]


if __name__ == "__main__":
    main()

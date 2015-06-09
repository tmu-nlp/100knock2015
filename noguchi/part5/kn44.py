# coding: utf-8

"""
dotファイルを生成します
dot -Tpng nekograph.dot -o nekograph.pngで図を生成
時間短縮のため20行目まで出力(19&20行目)
"""


import sys
import kn41 as chunk_senbei


def make_kakariuke_list(all_sent_list):
    kakariuke_list = list()
    sentence_number = 0

    for one_sent_list in all_sent_list:
        if sentence_number > 20:
            break
        kakariuke_num_list = list()
        chunk_number = 0
        for chunk in one_sent_list:
            if chunk.dst != str(-1):
                morph_kakarimoto = one_sent_list[chunk_number].morphs
                kakariuke_kakarimoto_list = list()
                for morph in morph_kakarimoto:
                    if morph.pos != "記号":
                        kakariuke_kakarimoto_list.append(morph.surface)
                kakariuke_kakarimoto = '"' + str(sentence_number) + ":" + "".join(kakariuke_kakarimoto_list) + '"'

                morph_kakarisaki = one_sent_list[int(chunk.dst)].morphs
                kakariuke_kakarisaki_list = list()
                for morph in morph_kakarisaki:
                    if morph.pos != "記号":
                        kakariuke_kakarisaki_list.append(morph.surface)
                kakariuke_kakarisaki = '"' + str(sentence_number) + ":" + "".join(kakariuke_kakarisaki_list) + '"'
                kakariuke_list.append((kakariuke_kakarimoto, kakariuke_kakarisaki))
            chunk_number += 1
        sentence_number += 1
    return kakariuke_list


def print_dot_file(kakariuke_list):
    print "digraph nekograph{"
    for kakariuke in kakariuke_list:
        kakariuke_kakarimoto = kakariuke[0]
        kakariuke_kakarisaki = kakariuke[1]
        print "    " + kakariuke_kakarimoto + " -> " + kakariuke_kakarisaki + ";"
    print "}"


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = chunk_senbei.make_chunk_class(fin)
    fin.close()
    kakariuke_list = make_kakariuke_list(all_sent_list)
    print_dot_file(kakariuke_list)


if __name__ == "__main__":
    main()

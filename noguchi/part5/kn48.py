# coding: utf-8

import sys
import kn41 as chunk_senbei


def stick_morphs_surface(chunk_info):
    morphs_info = chunk_info.morphs
    stick_surface = ""
    for morph in morphs_info:
        if morph.pos != "記号":
            stick_surface += morph.surface
    return stick_surface


def search_noun(chunk_info):
    noun_flag = False
    morphs_info = chunk_info.morphs
    for morph_info in morphs_info:
        if morph_info.pos == "名詞":
            noun_flag = True
            break
    return noun_flag


# pass in one_sent_passes in all_sent_passes
def make_kakariuke_pass_all_sent(all_sent_list):
    kakariuke_pass_all_sent = list()
    for one_sent_list in all_sent_list:
        count = 0
        kakariuke_pass_one_sent = list()
        for chunks in one_sent_list:
            kakariuke_pass = list()
            noun_flag = search_noun(chunks)
            if chunks.dst != str(-1) and noun_flag:
                chunk_src = one_sent_list[count]
                kakariuke_pass.append(stick_morphs_surface(chunk_src))
                # 係り先がなくなるまでの繰り返し(根まで移動)
                while chunk_src.dst != str(-1):
                    chunk_src = one_sent_list[int(chunk_src.dst)]
                    kakariuke_pass.append(stick_morphs_surface(chunk_src))
            count += 1
            if kakariuke_pass:
                kakariuke_pass_one_sent.append(kakariuke_pass)
        kakariuke_pass_all_sent.append(kakariuke_pass_one_sent)
    return kakariuke_pass_all_sent


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = chunk_senbei.make_chunk_class(fin)
    fin.close()
    kakariuke_pass_all_sent = make_kakariuke_pass_all_sent(all_sent_list)
    for kakariuke_pass_one_sent in kakariuke_pass_all_sent:
        for kakariuke_pass in kakariuke_pass_one_sent:
            print " -> ".join(kakariuke_pass)
        print ""


if __name__ == "__main__":
    main()

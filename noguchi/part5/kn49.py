# coding: utf-8

import sys
import kn41 as chunk_senbei


def stick_morphs_surface_label(label, chunk_info):
    morphs_info = chunk_info.morphs
    stick_surface = ""
    noun_flag = True
    for morph in morphs_info:
        if morph.pos == "名詞" and noun_flag:
            stick_surface += label
            noun_flag = False
        elif morph.pos != "記号":
            stick_surface += morph.surface
    return stick_surface


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
                kakariuke_pass.append(chunk_src)
                # 係り先がなくなるまでの繰り返し(根まで移動)
                while chunk_src.dst != str(-1):
                    chunk_src = one_sent_list[int(chunk_src.dst)]
                    kakariuke_pass.append(chunk_src)
            count += 1
            if kakariuke_pass:
                kakariuke_pass_one_sent.append(kakariuke_pass)
        kakariuke_pass_all_sent.append(kakariuke_pass_one_sent)
    return kakariuke_pass_all_sent


def replace_noun(label, kakariuke_pass_one_sent):
    new_kakariuke_pass_one_sent = list()
    count = 0
    for chunk_info in kakariuke_pass_one_sent:
        if count == 0:
            chunk_info = stick_morphs_surface_label(label, chunk_info)
            new_kakariuke_pass_one_sent.append(chunk_info)
        else:
            chunk_info = stick_morphs_surface(chunk_info)
            new_kakariuke_pass_one_sent.append(chunk_info)
        count += 1
    return new_kakariuke_pass_one_sent


def make_a_pass_noun_to_noun(two_kakariuke_pass):
    kakariuke_pass_i_sent, kakariuke_pass_j_sent = two_kakariuke_pass
    root_pass = list()
    kakariuke_pass_i_sent_operate = replace_noun("X", list(kakariuke_pass_i_sent))
    kakariuke_pass_j_sent_operate = replace_noun("Y", list(kakariuke_pass_j_sent))
    count = -1
    while len(kakariuke_pass_i_sent_operate) > 0 and len(kakariuke_pass_j_sent_operate) > 0 and kakariuke_pass_i_sent[count] == kakariuke_pass_j_sent[count]:
        root_pass.append(kakariuke_pass_j_sent_operate[-1])
        kakariuke_pass_i_sent_operate.pop(-1)
        kakariuke_pass_j_sent_operate.pop(-1)
        count -= 1
    root_pass.reverse()

    if kakariuke_pass_i_sent_operate and kakariuke_pass_j_sent_operate:
        return " -> ".join(kakariuke_pass_i_sent_operate) + " | " + " -> ".join(kakariuke_pass_j_sent_operate) + " | " + root_pass[0]
    else:
        kakariuke_pass_i_sent_operate.append("Y")
        return " -> ".join(kakariuke_pass_i_sent_operate)


def make_passes_noun_to_noun(kakariuke_pass_all_sent):
    passes_noun_to_noun = list()
    for kakariuke_pass_one_sent in kakariuke_pass_all_sent:
        if len(kakariuke_pass_one_sent) > 1:
            for i in range(len(kakariuke_pass_one_sent) - 1):
                for j in range(i + 1, len(kakariuke_pass_one_sent)):
                    a_pass_noun_to_noun = make_a_pass_noun_to_noun((kakariuke_pass_one_sent[i], kakariuke_pass_one_sent[j]))
                    passes_noun_to_noun.append(a_pass_noun_to_noun)
            passes_noun_to_noun.append("")
    return passes_noun_to_noun


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = chunk_senbei.make_chunk_class(fin)
    fin.close()
    kakariuke_pass_all_sent = make_kakariuke_pass_all_sent(all_sent_list)
    passes_noun_to_noun = make_passes_noun_to_noun(kakariuke_pass_all_sent)
    for a_pass_noun_to_noun in passes_noun_to_noun:
        print a_pass_noun_to_noun


if __name__ == "__main__":
    main()

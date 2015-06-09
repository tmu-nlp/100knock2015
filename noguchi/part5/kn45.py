# coding: utf-8

import sys
from collections import defaultdict
import kn41 as chunk_senbei


def make_verb2particle(all_sent_list):
    verb2particle = defaultdict(list)
    sentence_number = 0
    for one_sent_list in all_sent_list:
        count = 0
        for chunk in one_sent_list:
            if chunk.dst != str(-1):
                morph_kakarimoto = one_sent_list[count].morphs
                morph_kakarimoto_last = morph_kakarimoto[-1]
                if morph_kakarimoto_last.pos != "助詞":
                    case_pattern_particle = ""
                else:
                    case_pattern_particle = morph_kakarimoto_last.surface

                morph_kakarisaki = one_sent_list[int(chunk.dst)].morphs
                morph_kakarisaki_first = morph_kakarisaki[0]
                if len(morph_kakarisaki) > 1:
                    morph_kakarisaki_second = morph_kakarisaki[1]
                    if morph_kakarisaki_first.pos != "動詞" or "サ変" not in morph_kakarisaki_first.pos1 or morph_kakarisaki_second.surface != "を":
                        case_pattern_verb = ""
                    else:
                        
                        case_pattern_verb = morph_kakarisaki_first.base

                if case_pattern_verb and case_pattern_particle:
                    verb2particle[case_pattern_verb].append(case_pattern_particle)

            count += 1
        sentence_number += 1

    return verb2particle


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = chunk_senbei.make_chunk_class(fin)
    fin.close()
    verb2particle = make_verb2particle(all_sent_list)
    for verb, particle in verb2particle.items():
        print verb + "\t" + " ".join(sorted(particle))


if __name__ == "__main__":
    main()

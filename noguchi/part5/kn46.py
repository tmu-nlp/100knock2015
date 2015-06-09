# coding: utf-8

import sys
from collections import defaultdict
import kn41 as chunk_senbei


def make_verb2perticles_verb2caseframe(all_sent_list):
    verb2perticles = defaultdict(list)
    verb2caseframe = defaultdict(list)
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
                    caseframe = ""
                    for morph in morph_kakarimoto:
                        if morph.pos != "記号":
                            caseframe += morph.surface
                    case_pattern_caseframe = caseframe

                morph_kakarisaki = one_sent_list[int(chunk.dst)].morphs
                morph_kakarisaki_first = morph_kakarisaki[0]
                if morph_kakarisaki_first.pos != "動詞":
                    case_pattern_verb = ""
                else:
                    case_pattern_verb = morph_kakarisaki_first.base

                if case_pattern_verb and case_pattern_particle:
                    verb2perticles[case_pattern_verb].append(case_pattern_particle)
                    verb2caseframe[case_pattern_verb + " " + case_pattern_particle].append(case_pattern_caseframe)

            count += 1
        sentence_number += 1

    return (verb2perticles, verb2caseframe)


def main():
    fin = open(sys.argv[1], "r")
    all_sent_list = chunk_senbei.make_chunk_class(fin)
    fin.close()
    verb2perticles, verb2caseframe = make_verb2perticles_verb2caseframe(all_sent_list)
    for verb, particles in verb2perticles.items():
        print verb + "\t" + " ".join(sorted(particles)),
        print "\t",
        particles_set = set(particles)
        for particle in sorted(particles_set):
            print " ".join(sorted(verb2caseframe[verb + " " + particle])),
        print ""


if __name__ == "__main__":
    main()

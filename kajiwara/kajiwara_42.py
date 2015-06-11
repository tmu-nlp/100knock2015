# coding:utf-8

from kajiwara_41 import get_chunks_list


def main():
    sentence_number = 7
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha"
    sentences = get_chunks_list(fname)
    for phrase_number in range(len(sentences[sentence_number])):
        # 係り先文節番号
        destination_number = sentences[sentence_number][phrase_number].dst
        # 係り元文節番号
        for source_number in sentences[sentence_number][phrase_number].srcs:
            outputs = list()
            # 係り元の文節
            if source_number == -1:
                outputs.append("None")
            else:
                outputs.append("".join([morph.surface for morph in sentences[sentence_number][source_number].morphs if not morph.pos == "記号"]))
            # 対象の文節
            outputs.append("".join([morph.surface for morph in sentences[sentence_number][phrase_number].morphs if not morph.pos == "記号"]))
            # 係り先の文節
            if destination_number == -1:
                outputs.append("None")
            else:
                outputs.append("".join([morph.surface for morph in sentences[sentence_number][destination_number].morphs if not morph.pos == "記号"]))
            # タブ区切り形式で出力
            print "\t".join(outputs)


if __name__ == '__main__':
    main()

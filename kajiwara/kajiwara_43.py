# coding:utf-8

from kajiwara_41 import get_chunks_list


def is_nominal_phrase(chunk):
    if [morph.pos for morph in chunk.morphs if morph.pos == "名詞"]:
        return True
    else:
        return False


def is_verbal_phrase(chunk):
    if [morph.pos for morph in chunk.morphs if morph.pos == "動詞"]:
        return True
    else:
        return False


def main():
    sentence_number = 7
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/neko.txt.cabocha"
    sentences = get_chunks_list(fname)
    for phrase_number in range(len(sentences[sentence_number])):
        original_phrase = sentences[sentence_number][phrase_number]
        if not is_nominal_phrase(original_phrase):
            continue
        destination_phrase = sentences[sentence_number][original_phrase.dst]
        if not is_verbal_phrase(destination_phrase):
            continue
        outputs = list()
        outputs.append("".join([morph.surface for morph in original_phrase.morphs if not morph.pos == "記号"]))
        outputs.append("".join([morph.surface for morph in destination_phrase.morphs if not morph.pos == "記号"]))
        print "\t".join(outputs)


if __name__ == '__main__':
    main()

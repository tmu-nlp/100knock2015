# coding:utf-8

import xml.etree.ElementTree as ET
from collections import defaultdict


def parse_xml(fname):
    sentences = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
    coreferences = defaultdict(lambda: defaultdict(str))
    tree = ET.parse(fname)
    for sentence in tree.find(".//sentences").getiterator("sentence"):
        for token in sentence.find("tokens").getiterator("token"):
            sentences[sentence.get("id")][token.get("id")]["word"] = token.findtext("word")
    for coreference in tree.find(".//coreference").getiterator("coreference"):
        for mention in coreference.getiterator("mention"):
            if mention.get("representative") == "true":
                sub_text = mention.findtext("text")
            else:
                coreferences[mention.findtext("sentence")][mention.findtext("text")] = sub_text
    return sentences, coreferences


def coreference_analysis(sentences, coreferences):
    for sentence_id, tokens in sorted([(int(sentence_id), tokens) for sentence_id, tokens in sentences.items()]):
        sentence_id = str(sentence_id)
        sentence = ""
        for token_id in sorted([int(token_id) for token_id in tokens.keys()]):
            token_id = str(token_id)
            sentence += sentences[sentence_id][token_id]["word"]
            sentence += " "
        for mention, representative_mention in coreferences[sentence_id].items():
            sentence = sentence.replace(mention, representative_mention + "(" + mention + ")")
        print sentence.strip()


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt.xml"
    sentences, coreferences = parse_xml(fname)
    coreference_analysis(sentences, coreferences)


if __name__ == '__main__':
    main()

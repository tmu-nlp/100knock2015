#!usr/bin/python

import xml.dom.minidom

if __name__ == "__main__":

    dom = xml.dom.minidom.parse("nlp.txt.xml")
    word_list = []
    lemma_list = []
    pos_list = []
    for word in dom.getElementsByTagName("word"):
        word_list.append(word.firstChild.data)
    for lemma in dom.getElementsByTagName("lemma"):
        lemma_list.append(lemma.firstChild.data)
    for pos in dom.getElementsByTagName("POS"):
        pos_list.append(pos.firstChild.data)

    for i in range(1, len(word_list)):
        print word_list[i], "\t", lemma_list[i], "\t", pos_list[i]





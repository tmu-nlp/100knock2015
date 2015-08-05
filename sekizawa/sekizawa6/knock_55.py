#!usr/bin/python

import xml.dom.minidom

if __name__ == "__main__":

    dom = xml.dom.minidom.parse("nlp.txt.xml")

    for word, ner in zip(dom.getElementsByTagName("word"), dom.getElementsByTagName("NER")):
        if ner.firstChild.data == "PERSON":
            print word.firstChild.data



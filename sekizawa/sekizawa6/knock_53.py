#!usr/bin/python

import xml.dom.minidom

if __name__ == "__main__":

    dom = xml.dom.minidom.parse("nlp.txt.xml")

    for word in dom.getElementsByTagName("word"):
        print word.firstChild.data




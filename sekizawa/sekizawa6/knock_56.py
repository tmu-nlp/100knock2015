#!usr/bin/python

import xml.dom.minidom

if __name__ == "__main__":

    dom = xml.dom.minidom.parse("nlp.txt.xml")
    word_list = []
    ment_list = []
    count = 0

    for word in dom.getElementsByTagName("word"):
        word_list.append(word.firstChild.data)
        print "word"
    corefs =  dom.getElementsByTagName("coreference")
    for coref in corefs:
        reps = dom.getElementsByTagName("mention")
        for rep in reps:
            texts = dom.getElementsByTagName("text")
            for text in texts:
                ment_list.append(text.firstChild.data)
                print text.firstChild.data
    print word_list
    print ment_list


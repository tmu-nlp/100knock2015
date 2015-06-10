#!usr/vin/python


from part53 import *

def pos_tagging(file_name):
    tag_word = "<word>"; tag_lemma = "<lemma>"; tag_pos = "<POS>"
    gct = get_content_tags
    for line in open(file_name):
        if tag_word in line:
            word = gct(line, tag_word)
        elif tag_lemma in line:
            lemma = gct(line, tag_lemma)
        elif tag_pos in line:
            print  "\t".join((word, lemma, gct(line, tag_pos) ) )



if __name__ == "__main__":
    file_name = "nlp.txt.xml"
    pos_tagging(file_name)

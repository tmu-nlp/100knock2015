#!usr/bin/python

import re


def put_line_break(words):
    re_seg = re.compile("([,.:;!?]) ([A-Z])")
    words = re_seg.sub(lambda x: x.group().replace(" ", "\n"),  words)
    return words


def sentence_segment(file_name):
    return  put_line_break(open(file_name).read() )



if __name__ == "__main__":
    file_name = "nlp.txt" 
    print sentence_segment(file_name) 

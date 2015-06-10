#!usr/bin/python

from part53 import *
from collections import defaultdict

def get_next_num(len_tags, now):
    next_num = now + 1
    if len_tags == next_num:
        next_num = 0
    return next_num


def load_mention(xml_name):
    motion_dict = defaultdict(lambda:  defaultdict(list) )
    gct = get_content_tags
    tag_head = "<head>"; tag_end = "<end>";
    tag_start = "<start>"; tag_sentence = "<sentence>";
    tags = ["<head>", "<end>", "<start>",  "<sentence>"]
    tag_num = 0; len_tags = len(tags); tag = tags[tag_num]

    for line in open(xml_name).readlines()[::-1]:
        if "</dependencies>" in line:
            break
        elif tag in line:
            if tag == tag_head:
                head = gct(line, tag_head)
            elif tag == tag_end:
                end = gct(line, tag_end)
            elif tag == tag_start:
                start = gct(line, tag_start)
            elif tag == tag_sentence and int(end) - int(head) != 1:
                sentence = gct(line, tag_sentence)
                motion_dict[sentence][tag_end].append(end)
                motion_dict[sentence][tag_head].append(head)
                motion_dict[sentence][tag_start].append(start)
            tag_num = get_next_num(len_tags, tag_num)
            tag = tags[tag_num]
    
    return motion_dict


def get_parenthesis(motion_dict, token_id):
    if token_id in motion_dict["<head>"]:
        if token_id in motion_dict["<start>"]:
            return "[("
        return "("
    elif token_id in  motion_dict["<start>"]:
        return "["
    elif token_id in motion_dict["<end>"]:
        return ") ]"
    return ''

def coreference_analysis(xml_name):
    tag_sentence_id = "<sentence id="; sentence_id = 0
    tag_word = "<word>"
    tag_token_id = "<token id"; token_id = 0
    parenthesis = ''
    motion_dict = load_mention(xml_name)
    for line in open(xml_name):
        if tag_token_id in line:
            token_id += 1
            if str(sentence_id) in motion_dict:
                 parenthesis = get_parenthesis(motion_dict[str(sentence_id)], str(token_id))
                 if parenthesis != '':
                     print parenthesis,



        elif tag_sentence_id in line:
            sentence_id += 1
            token_id = 0
            print ''
        elif tag_word in line:
            print get_content_tags(line, tag_word),


        



if __name__ == "__main__":
    xml_name = "nlp.txt.xml"
    txt_name = "nlp.txt"

    coreference_analysis(xml_name)

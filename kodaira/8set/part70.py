#!/usr/bin/python
# count neg_pos : cut -c 1-2 | sort | uniq -c

import random

def add_label(file_name, label):
    labeled_file = list()
    for line in open(file_name):
        labeled_file.append(' '.join((label, line)) )
    return labeled_file
        
def make_random_text(pos_file_name, neg_file_name):
    pos_file = add_label(pos_file_name, '+1')
    neg_file = add_label(neg_file_name, '-1')
    text = pos_file + neg_file
    random.shuffle(text)
    return text
    

if __name__ == "__main__":
    pos_file_name = "rt-polarity.pos"
    neg_file_name = "rt-polarity.neg"
    print __name__
    exit()
    random_text = make_random_text(pos_file_name, neg_file_name)
    
    output_file = open('sentiment.txt', 'w')
    for line in random_text:
        output_file.write(line)
        print line
    output_file.close()

#!/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess


def word_print(sent_lst):
    for sent in sent_lst:
        words = sent.split(" ")
        for word in words:
            print word


if __name__ == "__main__":
    cmd = "python ex50.py"
    proc = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    sent_lst = proc.stdout
    word_print(sent_lst)

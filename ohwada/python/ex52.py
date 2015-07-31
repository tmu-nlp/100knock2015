#!/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess
from stemming.porter import stem


def word_and_stemmed(word_lst):
    for word in word_lst:
        word = word.strip()
        print word + "\t" + stem(word)


if __name__ == "__main__":
    cmd = "python ex51.py"
    proc = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    word_lst = proc.stdout
    word_and_stemmed(word_lst)

#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def trim_text(text):
    symbol_lst = ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', "'", '"']
    
    for line in text:
        token_lst = line.strip().split(" ")
        new_token_lst = []
        for token in token_lst:
            if token == "":
                continue
            if len(token) > 0 and token[0] in symbol_lst:
                token = token[1:]
            if len(token) > 0 and token[-1] in symbol_lst:
                token = token[:-1]
            if token != "":
                new_token_lst.append(token)

        f_out.write(" ".join(new_token_lst) + "\n")


if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    f_out = open("trimmed.txt", "w")
    trim_text(f)

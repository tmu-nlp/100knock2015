#!/usr/bin/python
# -*- coding:utf-8 -*-


import re


def extr_sent(f):
    text = f.read()
    match_iter = re.finditer(r'[.;:?!]\s[A-Z]', text)
    old_m = None
    for m in match_iter:
        if old_m is not None:
            sent = text[old_m.end()-1:m.start()+1]
        else:
            sent = text[:m.start()+1]
        print sent
        old_m = m



if __name__ == "__main__":
    with open("nlp.txt", "r") as f:
        extr_sent(f)        

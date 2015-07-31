#!/usr/bin/python
# -*- coding:utf-8 -*-

import re


def make_country_name_lst():
    f = open("countries.txt", "r")
    country_name_lst = [l.split("|")[1] for l in f.readlines()]

    return country_name_lst


def detect_compound_country(text, f_out):
    country_lst = make_country_name_lst()
    
    for name in country_lst:
        pattern = re.compile(r"{0}".format(name))
        text = pattern.sub(lambda x:"_".join(x.group().split(" ")), text)
     
    f_out.write(text)



if __name__ == "__main__":
    f = open("trimmed.txt", "r")
    f_out = open("corpus.txt", "w")
    detect_compound_country(f.read(), f_out)

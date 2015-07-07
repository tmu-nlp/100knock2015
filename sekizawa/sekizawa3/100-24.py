#!usr/bin/python
#coding:utf-8

import re

if __name__ == "__main__":

    f = open("UK.json", "r")

    pattern = re.compile("(\[\[File\:)(.+?)(\|)")
    for line in f:
        judge = pattern.search(line)
        if judge:
            print judge.group(2)

    f.close()



#!usr/bin/python
#coding:utf-8

import re
from collections import defaultdict

if __name__ == "__main__":

    f = open("UK.json", "r")

    my_dict = defaultdict(lambda: 0)
    pattern = re.compile("(\|)(.+)(\=)(.+)")
    for line in f:
        if(line != "}}\n"):
            judge = pattern.search(line)
            if judge:
                my_dict[judge.group(2)] = judge.group(4)
                print judge.group(2),
                print judge.group(4)
        else:
            break

    f.close()



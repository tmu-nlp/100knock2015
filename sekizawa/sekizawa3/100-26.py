#!usr/bin/python
#coding:utf-8

import re
from collections import defaultdict

if __name__ == "__main__":

    f = open("UK.json", "r")
    w = open("100-26.txt", "w")

    my_dict = defaultdict(lambda: 0)
    pattern1 = re.compile("(\|)(.+)(\=)(.+)")
    pattern2 = re.compile("(\'\'+)")
    for line1 in f:
        if(line1 != "}}\n"):
            line2 = pattern2.sub("", line1)
            judge = pattern1.search(line2)

            if judge:
                my_dict[judge.group(2)] = judge.group(4)
                w.write(judge.group(2))
                w.write(judge.group(4))
                w.write("\n")
        else:
            break

    f.close()
    w.close()




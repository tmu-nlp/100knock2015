#!usr/bin/python
#coding:utf-8

import re
from collections import defaultdict

if __name__ == "__main__":

    f = open("UK.json", "r")
    w = open("100-27.txt", "w")

    my_dict = defaultdict(lambda: 0)
    pattern1 = re.compile("(\|)(.+)(\=)(.+)")
    pattern2 = re.compile("(\'\'+)")
    pattern3 = re.compile("(\[http\:\/\/)(.+)(\])")
    for line1 in f:
        line2 = pattern2.sub("", line1)
        line3 = pattern3.sub("", line2)
        judge = pattern1.search(line3)
        if judge:
            
            my_dict[judge.group(2)] = judge.group(4)
            w.write(judge.group(2))
            w.write(judge.group(4))
            w.write("\n")

    f.close()
    w.close()





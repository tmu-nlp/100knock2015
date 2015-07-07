#!usr/bin/python
#coding:utf-8

import re
from collections import defaultdict

if __name__ == "__main__":

    f = open("UK.json", "r")
    w = open("100-28.txt", "w")

    my_dict = defaultdict(lambda: 0)
    pattern1 = re.compile("(\|)(.+)(\=)(.+)")
    pattern2 = re.compile("(\'\'+)")
    pattern3 = re.compile("(\[\[)")
    pattern4 = re.compile("(\]\])")
    pattern5 = re.compile("(\[)(http\:)(.+)(\])")

    for line1 in f:
        if(line1 != "}}\n"):
            line2 = pattern2.sub("", line1)
            line3 = pattern3.sub("", line2)
            line4 = pattern4.sub("", line3)
            line5 = pattern5.sub("", line4)
            judge = pattern1.search(line5)
            if judge:
            
                my_dict[judge.group(2)] = judge.group(4)
                w.write(judge.group(2))
                w.write(judge.group(4))
                w.write("\n")
        else:
            break

    f.close()
    w.close()






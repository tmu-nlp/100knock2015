# coding:utf-8
"""
python knock081.py ../Data/result/knock080/clean.txt ../Data/country_name_list.txt
"""

import sys
import re

for line in open(sys.argv[1]):
    for contry in open(sys.argv[2]):
        pattern  = re.compile(contry.strip())
        line = pattern.sub(lambda m: m.group().replace(' ', '_'), line)
    print line

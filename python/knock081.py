# coding:utf-8
"""
python knock081.py ../Data/result/knock080/clean.txt ../Data/country_name_list.txt
"""

import sys
import re

contries = list()
for contry in open(sys.argv[2]):
    contries.append(contry.strip())

for line in open(sys.argv[1]):
    for contry in contries:
        if contry in line:
            line = re.sub(contry, lambda m: m.group().replace(' ', '_'), line)
    print line

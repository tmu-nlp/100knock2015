#! usr/bin/python
# -*- coding: utf-8 -*-
# コマンドは tail -n N file

import sys

my_file = open(sys.argv[2], "r")
para = int(sys.argv[1])
lines = []

for line in my_file:
  line = line.strip()
  lines.append(line)

print "\n".join(lines[len(lines) - para:len(lines)])

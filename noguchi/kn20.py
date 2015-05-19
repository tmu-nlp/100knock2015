#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json

my_file = open(sys.argv[1])

for line in my_file:
  dec_line = json.loads(line)
  if dec_line["title"] == u"イギリス":
    print dec_line["text"].encode("utf-8")

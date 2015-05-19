#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import json
from urllib import urlopen

my_dict = {}
kiso = re.compile("\|(.+?) = (.*)")
ref = re.compile("<ref[ |>].*")
kyou = re.compile("''+")
link1 = re.compile("\[\[([^\]]*)\]\]")
link2 = re.compile("\[\[([^\]]*)\|([^\]]*)\]\]")
mark = re.compile("\(&.+\)")
br = re.compile("<br ?/>")
wiki_api = "http://ja.wikipedia.org/w/api.php?action=query&format=json&titles=Image:%s&prop=imageinfo&iiprop=url"

for line in open(sys.argv[1], "r"):
  line = line.strip()
  kiso_match = kiso.search(line)
  if kiso_match:
    k_right = kiso_match.group(2)
    k_right = ref.sub("", k_right)
    k_right = kyou.sub("", k_right)
    k_right = link2.sub(lambda sub: sub.group(1) + " " +  sub.group(2), k_right)
    k_right = link1.sub(lambda sub: sub.group(1), k_right)
    k_right = mark.sub("", k_right)
    k_right = br.sub("", k_right)
    if kiso_match.group(1) == "国旗画像":
      res = urlopen(wiki_api % k_right).read()
      jres = json.loads(res)
      k_right = jres["query"]["pages"]["-1"]["imageinfo"][0]["url"].encode("utf-8")
    my_dict[kiso_match.group(1)] = k_right

for j, k in my_dict.items():
  print j + "\t= " + k

import sys
import re

my_dict = {}
kiso = re.compile("\|(.+?) = (.*)")
ref = re.compile("<ref[ |>].*")
kyou = re.compile("''+")
link1 = re.compile("\[\[([^\]]*)\]\]")
link2 = re.compile("\[\[([^\]]*)\|([^\]]*)\]\]")

for line in open(sys.argv[1], "r"):
  line = line.strip()
  kiso_match = kiso.search(line)
  if kiso_match:
    k_right = kiso_match.group(2)
    k_right = ref.sub("", k_right)
    k_right = kyou.sub("", k_right)
    k_right = link2.sub(lambda sub: sub.group(1) + " " +  sub.group(2), k_right)
    k_right = link1.sub(lambda sub: sub.group(1), k_right)
    my_dict[kiso_match.group(1)] = k_right

for j, k in my_dict.items():
  print j + " = " + k

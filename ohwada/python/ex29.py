#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pickle
import urllib
import json


f = open("template_dic.pcl", "r")
d = pickle.load(f)

for key, value in d.items():
    if key == "国旗画像":
        break


base_url = "http://ja.wikipedia.org/w/api.php?"
parameters = [("format", "json"), ("action", "query"), ("titles", "Image:{0}".format(value)),
              ("prop", "imageinfo"), ("iiprop", "url")]

url = base_url + "&".join([p + "=" + v for p, v in parameters])

print url


f = urllib.urlopen(url)
data = json.load(f)
print data["query"]["pages"]["-1"]["imageinfo"][0]["url"]

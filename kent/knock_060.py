#!/usr/bin/python
#_*_coding:utf-8_*_


import sys
import json

loading_json_file = open("artist.json", "r")

for line in loading_json_file:
    line = line.strip()
    jsonData = json.loads(line)

    print jsonData["name"]

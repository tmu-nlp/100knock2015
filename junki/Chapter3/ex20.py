#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import json #jsonをインポート

readfile = open(sys.argv[1])

for line in readfile:
	data = json.loads(line.strip())#json読み込み
	if data["title"] == u"イギリス":
		print data["text"].encode("utf-8")#イギリスのデータテキストをutf-8で表示
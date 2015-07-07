#!usr/bin/python
#-*-coding:utf-8-*-

import plyvel
import json
import sys
import pickle

def KVS(artist_file):
	my_DataBase = plyvel.DB('test63.ldb', create_if_missing=True) 
	for line in artist_file:
		jdict = json.loads(line.strip())
		try:
			tags_list = pickle.dumps(jdict[u"tags"])#無理やり pickleのdumpを用いてストリングにする（でーたべーすは）
			my_DataBase.put(jdict["name"].encode('utf-8'),tags_list)
		except(KeyError):#tagsがない場合
			pass #print "KeyError"#エラー表示
	#return my_DataBese

	for name, tags in my_DataBase:
		print "\n"
		print name
		for dictionary in pickle.loads(tags_list):#tags_listをリストにする
			for key, value in dictionary.items():
				print "\t"+str(key), "\t"+str(value)

			


def main(jsonfile):
	KVS(jsonfile)

if __name__ == '__main__':
    main(open(sys.argv[1]))
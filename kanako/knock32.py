#!usr/bin/python
#coding: utf-8
from knock30 import morph_read

if __name__=='__main__':
	for sent in morph_read():
		for m_dict in sent:
			if m_dict['pos'] == '動詞':
				print m_dict["base"]


#!usr/bin/python
#coding: utf-8
from knock30 import morph_read

def noun_con():
	noun = []; noun_list =[]
	noun_num = 0
	for sent in morph_read():
		for m_dict in sent:
			if m_dict['pos'] == '名詞':
				noun.append(m_dict['surface'])
			else:
				if noun_num < len(noun):
					noun_list = []
					noun_list.append(noun)
					noun_num = len(noun)
				elif noun_num == len(noun):
					noun_list.append(',')
					noun_list.append(noun)
				noun = []
	return noun_list
if __name__=='__main__':
	for i in noun_con():
		for j in i:
			print j,

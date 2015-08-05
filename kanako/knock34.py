#!usr/bin/python
#coding:utf-8
from knock30 import morph_read

def two_noun():
	noun_ph = []; noun_ph_list = []
	for sent in morph_read():
		flag = 0
		for m_dict in sent:
			if m_dict['pos'] == '名詞' and flag == 0:
				noun_ph.append(m_dict['surface'])
				flag = 1
			elif m_dict['pos'] == '名詞' and flag == 1:
				noun_ph = []
				noun_ph.append(m_dict['surface'])
				flag = 1
			elif m_dict['surface'] == 'の' and flag == 1:
				noun_ph.append(m_dict['surface'])
				flag = 2
			elif m_dict['pos'] == '名詞' and flag == 2:
				noun_ph.append(m_dict['surface'])
				''.join(noun_ph)
				noun_ph_list.append(noun_ph)
				noun_ph = []
				flag = 0
			else:
				noun_ph =[]
				flag = 0
	return noun_ph_list
if __name__=='__main__':
	two_noun()
	for i in two_noun():
		print
		for j in i:
			print j,


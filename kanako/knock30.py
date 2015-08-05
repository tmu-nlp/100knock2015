#!/usr/bin/python
#coding: UTF-8

def morph_read():
	sent = []
	morph_spl = []
	sent_list = []
	morph_dict = {}
	for line in open("neko.txt.mecab"):
		spl_tab = line.strip().split("\t")
		if line.startswith("EOS"):
			if len(sent) == 0:
				continue		
			sent_list.append(sent)
			sent = []
			continue
		morph_spl = spl_tab[1].split(",")
		morph_dict["surface"] = spl_tab[0]
		morph_dict["base"] = morph_spl[6]
		morph_dict["pos"] = morph_spl[0]
		morph_dict["pos1"] = morph_spl[1]
		sent.append(morph_dict.copy())
	return sent_list
if __name__=='__main__':
	for n in morph_read():
		for m in n:
			for i,j in m.items():
				print i,j
		print
	

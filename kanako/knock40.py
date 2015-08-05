#!/usr/bin/python
#coding: UTF-8

class Morph:
		def __init__(self,surface,base,pos,pos1):
				self.surface = surface
				self.base = base
				self.pos = pos
				self.pos1 = pos
def morph_text_maker():
		sent = []
		text = []
		for line in open("neko.txt.cabocha"):
				if line.startswith("*"):
						continue
				elif line.startswith("EOS"):
						text.append(sent)
						sent = []
				else:
						sur = line.strip().split("\t")
						bpp =  sur[1].split(",")
						sent.append(Morph(sur[0],bpp[6],bpp[0],bpp[1]))	
		return text
if __name__=='__main__':
	for morph in morph_text_maker()[2]:
		print morph.surface, morph.base, morph.pos, morph.pos1
		

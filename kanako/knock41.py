#!/usr/bin/python
#coding: UTF-8
from collections import defaultdict
from knock40 import Morph

class Chunk:
		def __init__(self,morphs,dst,srcs):
			self.morphs = morphs
			self.dst = dst
			self.srcs = srcs
def chunk_maker():
	sent = []; text = []; morphs = []
	lattice_list = []
	srcs = defaultdict(list); 
	for line in open("neko.txt.cabocha"):
		if line.startswith("*"):
			lattice_list = line.strip().split(" ")
			dst = lattice_list[2].rstrip('D')
			srcs[dst].append(lattice_list[1])
			sent.append(Chunk(morphs,dst,srcs[lattice_list[1]]))
			morphs = []
			srcs[dst] = []
		elif line.startswith("EOS"):
			text.append(sent)
			sent = []
		else:
			sur = line.strip().split("\t")
			bpp =  sur[1].split(",")
			morphs.append(Morph(sur[0],bpp[6],bpp[0],bpp[1]))
	return text
if __name__=='__main__':
	for (i,sent) in enumerate(chunk_maker()):
		if i == 7:
			for chunk in sent:
				print chunk.dst,
				for m in chunk.morphs:
					print m.surface,
				print

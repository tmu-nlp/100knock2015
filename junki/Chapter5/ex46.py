#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from ex41_1 import *

def main():
	all_sent_list = make_chunk_list()
	verb_particle = defaultdict(list)

	for line in all_sent_list:
		for chunk in line:
			if int(chunk.dst) != -1:
				sent = ''
				every = []
				Noun_yes = 0
				Verb_yes = 0
				for morph in chunk.morphs:
					every.append(morph.surface)
					if morph.pos == '助詞':
						every = []
						Noun_yes = 1
						every.append(morph.surface)
					
					if morph.pos == '名詞':
									
				
				#sent += '\t'

				everypos = ''
				for morph in line[int(chunk.dst)].morphs:
					#print morph.base
					#everypos = ''
					everypos += morph.base
					if morph.pos == '動詞':
						Verb_yes = 1
						break

				if Noun_yes == 1 and Verb_yes == 1 :
					if everypos in '。':
						everypos = everypos.replace('。','')
					if everypos in '、':
						everypos = everypos.replace('、','')
					#print everypos,
					for particle in every:
						print particle, everypos
						verb_particle[everypos].append(particle)

					#verb_particle.append(everypos
	#for v, p in verb_particle.items():
		#print v,
		#for p1 in p:
			#print p1
		#print ""

if __name__ == '__main__':
	main()
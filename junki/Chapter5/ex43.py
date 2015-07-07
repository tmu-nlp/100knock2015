#!usr/bin/python
#-*-coding:utf-8-*-

from ex41_1 import *

def main():
	all_sent_list = make_chunk_list()
	
	for line in all_sent_list:
		for chunk in line:
			if int(chunk.dst) != -1:
				sent = ''
				every = ''
				Noun_yes = 0
				Verb_yes = 0
				for morph in chunk.morphs:
					every += morph.surface
					if morph.pos == '名詞':
						Noun_yes = 1
				
				sent += '\t'

				everypos = ''
				for morph in line[int(chunk.dst)].morphs:
					everypos += morph.surface
					if morph.pos == '動詞':
						Verb_yes = 1

				if Noun_yes ==1 and Verb_yes ==1 :
					everypos = everypos.replace('。','')
					everypos = everypos.replace('、','')
					print every, everypos

if __name__ == '__main__':
	main()




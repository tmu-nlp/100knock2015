#!usr/bin/python
#-*-coding:utf-8-*-


from ex41_1 import *


def main():
	all_sent_list = make_chunk_list()

	for line in all_sent_list:
		for chunk in line:
			if int(chunk.dst) != -1:
				sent = ''
				for morph in chunk.morphs:
					sent += morph.surface
				sent += '\t'
				for morph in line[int(chunk.dst)].morphs:
					sent += morph.surface
				print sent

if __name__ == '__main__':
	main()

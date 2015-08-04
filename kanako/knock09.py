#!/usr/bin/python
#coding: UTF-8
import random

def word_random(text):
	random_text = []
	random_word = []
	word = text.split(" ")
	for w in word:
		if len(w) <= 4:
			random_text.append(w)
		else:
			w_list = list(w[1:-1]) 
			random.shuffle(w_list)
			random_word = "".join(w_list)
			random_words = str(w[0]) + random_word + str(w[-1])
			random_text.append(random_words)
	return " ".join(random_text)

if __name__=='__main__':
	print word_random("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")

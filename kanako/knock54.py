#!usr/bin/python
#coding:utf-8
from xml.dom import minidom

def xml_word_lemma_pos():
	doc = minidom.parse('nlp.txt.xml')
	word = []; lemma = []; pos = [];
	for w in doc.getElementsByTagName('word'):
		word.append(w.childNodes[0].data)
	for l in doc.getElementsByTagName('lemma'):
		lemma.append(l.childNodes[0].data)
	for p in doc.getElementsByTagName('POS'):
		pos.append(p.childNodes[0].data)
	for i in range(len(word)):
		print word[i],'\t',lemma[i],'\t',pos[i]

if __name__ == '__main__':
	xml_word_lemma_pos()



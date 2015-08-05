#!usr/bin/python
#coding:utf-8
from xml.dom import minidom

def xml_word():
	doc = minidom.parse('nlp.txt.xml')
	word = []
	for w in doc.getElementsByTagName('word'):
		word.append(w.childNodes[0].data)
	return word

if __name__ == '__main__':
	for w in xml_word():
		print w



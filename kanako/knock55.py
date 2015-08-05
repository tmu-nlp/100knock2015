#!usr/bin/python
#coding:utf-8
from xml.dom import minidom

def nlp_person():
	doc = minidom.parse('nlp.txt.xml')
	person = []
	for t in doc.getElementsByTagName('token'):
		if t.getElementsByTagName('NER').item(0).childNodes[0].data == 'PERSON':
			person.append(t.getElementsByTagName('word').item(0).childNodes[0].data)
	return person

if __name__ == '__main__':
	for w in nlp_person():
		print w



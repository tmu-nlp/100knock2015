#!/usr/bin/python
# -*- coding:utf-8 -*-

from xml.etree import ElementTree


def extr_tuple(xml):
    tree = ElementTree.parse(xml)
    root = tree.getroot()

    deps = [e for e in root.findall(".//dependencies") if e.get("type") == "collapsed-dependencies"]

    for dep in deps:
        dic_s = {}
        dic_o = {}
        for elem in dep:
            if elem.get("type") == "nsubj":
                sgov = elem.find("governor").text
                subj = elem.find("dependent").text
                dic_s[sgov] = subj
            elif elem.get("type") == "dobj":
                ogov = elem.find("governor").text
                obj = elem.find("dependent").text
                dic_o[ogov] = obj
        for sgov, subj in dic_s.items():
            if sgov in dic_o.keys():
                print "\t".join([subj, sgov, dic_o[sgov]])



if __name__ == "__main__":
    f = "nlp.txt.xml"
    extr_tuple(f)

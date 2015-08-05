# coding:utf-8

import xml.etree.ElementTree as ET
from collections import defaultdict


def parse_xml_relations(fname):
    tuples = list()
    tree = ET.parse(fname)
    for sentence in tree.find(".//sentences").getiterator("sentence"):
        for dependency in sentence.getiterator("dependencies"):
            if not dependency.get("type") == "collapsed-dependencies":
                continue
            predicate2dep_type2sbj_obj = defaultdict(lambda: defaultdict(str))
            for dep in dependency.getiterator("dep"):
                dep_type = dep.get("type")
                original = dep.findtext("governor")
                original = original + "(" + dep.find("governor").get("idx") + ")"
                destination = dep.findtext("dependent")
                destination = destination + "(" + dep.find("dependent").get("idx") + ")"
                predicate2dep_type2sbj_obj[original][dep_type] = destination
            for predicate, dep_type2sbj_obj in predicate2dep_type2sbj_obj.items():
                if dep_type2sbj_obj["nsubj"] and dep_type2sbj_obj["dobj"]:
                    subject = dep_type2sbj_obj["nsubj"].split("(")[0]
                    object = dep_type2sbj_obj["dobj"].split("(")[0]
                    predicate = predicate.split("(")[0]
                    tuples.append((subject, predicate, object))
    return tuples


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt.xml"
    tuples = parse_xml_relations(fname)
    for subject, predicate, object in tuples:
        print subject + "\t" + predicate + "\t" + object


if __name__ == '__main__':
    main()

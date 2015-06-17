# coding:utf-8

import pydot
import subprocess
import xml.etree.ElementTree as ET


def write_jpeg(edges, fname):
    graph = pydot.graph_from_edges(edges, directed=True)
    graph.write_jpeg(fname, prog="dot")


def parse_xml_relations(fname):
    edges = list()
    tree = ET.parse(fname)
    for sentence in tree.find(".//sentences").getiterator("sentence"):
        for dependency in sentence.getiterator("dependencies"):
            if not dependency.get("type") == "collapsed-dependencies":
                continue
            for dep in dependency.getiterator("dep"):
                original = dep.findtext("governor")
                original = original + "(" + dep.find("governor").get("idx") + ")"
                destination = dep.findtext("dependent")
                destination = destination + "(" + dep.find("dependent").get("idx") + ")"
                edges.append((original, destination))
            return edges
    return edges


def main():
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/nlp.txt.xml"
    edges = parse_xml_relations(fname)
    fname = "/Users/moguranosenshi/WorkSpace/100knock2015/kajiwara/data/relations_corenlp.jpg"
    write_jpeg(edges, fname)
    subprocess.call("open " + fname, shell=True)


if __name__ == '__main__':
    main()

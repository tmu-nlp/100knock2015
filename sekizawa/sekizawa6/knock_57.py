#!usr/bin/python

import xml.dom.minidom

if __name__ == "__main__":
    dom = xml.dom.minidom.parse("nlp.txt.xml")
    deps = dom.getElementsByTagName("dependencies")
    for i in range(deps.length):
        dep = deps.item(i).getElementsByTagName("dependant")
        print dep.firstchild.data
    for i in deps.getElementsByTagName:
        if dep.getElementsByTagName("link").item(0).getAttribute("type")\
             == "collapsed-dependencies":
            print "f"
        i += 1


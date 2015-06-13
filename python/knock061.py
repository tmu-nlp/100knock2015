# coding:utf-8
'''
python knock061.py ../Data/result/knock060/python/db.kch
'''

from kyotocabinet import *
import sys

db = DB()
if not db.open(sys.argv[1]):
    print >>sys.stderr, "open error: " + str(db.error())

for line in iter(sys.stdin.readline, '\n'):
    value = db.get(line.strip())
    print value

if not db.close():
    print >>sys.stderr, "close error: " + str(db.error())

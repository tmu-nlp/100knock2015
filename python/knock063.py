# coding:utf-8
'''
python knock063.py ../Data/artist.json ../Data/result/knock063/python/db.kch
'''

import sys
import json
import pickle
from kyoto_cabinet_wrapper import *

db = KyotoCabinet()
db.open(sys.argv[2], kc.DB.OWRITER|kc.DB.OCREATE)

# store
for line in open(sys.argv[1]):
    jdata = json.loads(line)
    if 'name' in jdata and 'tags' in jdata:
        db.set(jdata['name'], pickle.dumps(jdata['tags']))

print 'finished to store'
print 'enter the artist name'
# retrieval
for line in iter(sys.stdin.readline, '\n'):
    pickled = db.get(line.strip())
    if not pickled:
        print pickled
        continue
    tags = pickle.loads(pickled)
    for tagdic in tags:
        print ' '.join(str(v) for v in tagdic.values())

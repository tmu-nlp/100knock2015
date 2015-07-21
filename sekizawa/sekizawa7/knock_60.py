#!usr/bin/python
#coding:utf-8

import json
import kyotocabinet as kc

class KyotoCabinet(kc.DB):
    def __del__(self):
        self.close()

    def open(self, *args, **kwds):
        if not super(KyotoCabinet, self).open(*args, **kwds):
            raise IOError("Open error: {0}".format(super(KyotoCabinet, self).error()))

    def set(self, *args, **kwds):
        if not super(KyotoCabinet, self).set(*args, **kwds):
            raise IOError("Set error: {0}".format(super(KyotoCabinet, self).error()))

    def close(self, *args, **kwds):
        if not super(KyotoCabinet, self).close(*args, **kwds):
            raise IOError("Close error: {0}".format(super(KyotoCabinet, self).error()))

    def cursor(self, *args, **kwds):
        cur = super(KyotoCabinet, self).cursor(*args, **kwds)
        cur.jump()
        while 1:
            rec = cur.get_str(True)
            if not rec: break
            yield rec
        cur.disable()

if __name__ == "__main__":
    db = KyotoCabinet()
    db.open("artist.kch", kc.DB.OWRITER | kc.DB.OCREATE)
    json_file = open("artist.json", "r")
    for line in json_file:
        line = line.decode("utf-8")
        data = json.loads(line)
        if "name" in data and "area" in data:
            db.set(data["name"].encode("utf-8"), data["area"].encode("utf-8"))
    for rec in db.cursor():
        print(rec[0], ":", rec[1])
    json_file.close()


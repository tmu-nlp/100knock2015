#coding: utf-8
# Jsonファイルの読み込み

if __name__ == "__main__":
  import json
  import sys
  
  file = open(sys.argv[1])
  
  for line in file:
    data = json.loads(line)
    
    if data['title'] == u'アイルランド共和国':
      print data['text'].encode('utf-8')


  file.close()

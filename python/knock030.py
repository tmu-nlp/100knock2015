# coding:utf-8
'''
python python/knock030.py ../Data/neko.txt.mecab [out.pkl]
'''

import sys
import pickle

doc = list()
sent = list()
for line in open(sys.argv[1]):
    spl = line.strip().split('\t')

    # EOSがきたら一文の終わり
    if spl[0] == 'EOS':
        if len(sent) == 0:
            continue
        doc.append(sent)
        sent = list()
        continue

    # なんもない行だったらもともと空行
    if spl[0] == '':
        continue
    
    # どちらでもなければ形態素情報あり
    morph = dict()
    morph['surface'] = spl[0]
    morph['base'] = spl[3]
    morph['pos'] = spl[4]
    
    # 品詞細分類はあるやつとないやつがある
    if len(spl) < 6:
        morph['pos1'] = ''
    else:
        morph['pos1'] = spl[5]
    sent.append(morph)

# オブジェクトをそのまま（シリアライズして）出力
pickle.dump(doc, open(sys.argv[2], 'w'))
#for sent in doc:
#    for m in sent:
#        print '%s, %s, %s, %s' % (m['surface'], m['base'], m['pos'], m['pos1'])

